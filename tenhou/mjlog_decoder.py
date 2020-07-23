from typing import List, Tuple, Dict, Iterator
import json
import copy
import subprocess
import urllib.parse
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
from google.protobuf import json_format

import mahjong_pb2


class MjlogParser:
    def __init__(self):
        self.state = None

    def parse(self, path_to_mjlog: str) -> Iterator[mahjong_pb2.State]:
        tree = ET.parse(path_to_mjlog)
        root = tree.getroot()
        yield from self._parse_each_game(root)

    def _parse_each_game(self, root: Element) -> Iterator[mahjong_pb2.State]:
        assert (root.tag == "mjloggm")
        assert (root.attrib['ver'] == "2.3")
        shuffle = root.iter("SHUFFLE")
        go = root.iter("GO")
        un = root.iter("UN")  # TODO(sotetsuk): if there are > 2 "UN", some user became offline
        # print(urllib.parse.unquote(child.attrib["n0"]))
        taikyoku = root.iter("TAIKYOKU")

        self.state = mahjong_pb2.State()
        kv: List[Tuple[str, Dict[str, str]]] = []
        for child in root:
            if child.tag in ["SHUFFLE", "GO", "UN", "TAIKYOKU"]:
                continue
            if child.tag == "INIT":
                if kv:
                    yield from self._parse_each_round(kv)
                self.state = mahjong_pb2.State()
                kv = []
            kv.append((child.tag, child.attrib))
        if kv:
            yield from self._parse_each_round(kv)

    def _parse_each_round(self, kv: List[Tuple[str, Dict[str, str]]]) -> Iterator[mahjong_pb2.State]:
        """Input examples

        - <INIT seed="0,0,0,2,2,112" ten="250,250,250,250" oya="0" hai0="48,16,19,34,2,76,13,7,128,1,39,121,87" hai1="17,62,79,52,56,57,82,98,32,103,24,70,54" hai2="55,30,12,26,31,90,3,4,80,125,66,102,78" hai3="120,130,42,67,114,93,5,61,20,108,41,100,84"/>
          - key = INIT val = {'seed': '0,0,0,2,2,112', 'ten': '250,250,250,250', 'oya': '0', 'hai0': '48,16,19,34,2,76,13,7,128,1,39,121,87', 'hai1': '17,62,79,52,56,57,82,98,32,103,24,70,54', 'hai2': '55,30,12,26,31,90,3,4,80,125,66,102,78', 'hai3': '120,130,42,67,114,93,5,61,20,108,41,100,84'}
        - <F37/>:
          - key = "F37", val = ""
        - <REACH who="1" step="1"/>
          - key = "REACH", val = {'who': '1', 'step': '1'}
        - <REACH who="1" ten="250,240,250,250" step="2"/>
          - key = "REACH", val = {'who': '1', 'ten': '250,240,250,250', 'step': '2'}
        - <N who="3" m="42031" />
          - key = "N", val = {'who': '3', 'm': '42031'}
        - <DORA hai="8" />
          - key = "DORA", val = {'hai': '8'}
        - <RYUUKYOKU ba="0,1" sc="250,-10,240,30,250,-10,250,-10" hai1="43,47,49,51,52,54,56,57,62,79,82,101,103" />
          - key = "RYUUKYOKU" val = {'ba': '0,1', 'sc': '250,-10,240,30,250,-10,250,-10', 'hai1': '43,47,49,51,52,54,56,57,62,79,82,101,103'}
        - <AGARI ba="1,3" hai="1,6,9,24,25,37,42,44,45,49,52,58,60,64" machi="44" ten="30,8000,1" yaku="1,1,7,1,52,1,54,1,53,1" doraHai="69" doraHaiUra="59" who="2" fromWho="3" sc="240,0,260,0,230,113,240,-83" />
          - key = "AGARI" val = {'ba': '1,3', 'hai': '1,6,9,24,25,37,42,44,45,49,52,58,60,64', 'machi': '44', 'ten': '30,8000,1', 'yaku': '1,1,7,1,52,1,54,1,53,1', 'doraHai': '69', 'doraHaiUra': '59', 'who': '2', 'fromWho': '3', 'sc': '240,0,260,0,230,113,240,-83'}
        """
        assert (kv[0][0] == 'INIT')
        last_drawer, last_draw = None, None
        taken_action = None

        key, val = kv[0]
        assert(key == "INIT")
        round_, honba, riichi, dice1, dice2, dora = [int(x) for x in val["seed"].split(",")]
        self.state.score.round = round_
        self.state.score.honba = honba
        self.state.score.riichi = riichi
        self.state.dora.append(dora)
        self.state.score.ten[:] = [int(x) for x in val["ten"].split(",")]

        for key, val in kv[1:]:
            if key[0] in ["T", "U", "V", "W"]:  # draw
                # TODO (sotetsuk): consider draw after kan case
                who = MjlogParser._to_wind(key[0])
                draw = int(key[1:])
                taken_action = mahjong_pb2.TakenAction(
                    who=who,
                    type=mahjong_pb2.ACTION_TYPE_DRAW,
                    draw=draw,
                )
                last_drawer, last_draw = who, draw
            elif key[0] in ["D", "E", "F", "G"]:  # discard
                # TDOO (sotetsuk): riichi
                who = MjlogParser._to_wind(key[0])
                discard = int(key[1:])
                discard_drawn_tile = last_drawer == who and last_draw == discard
                taken_action = mahjong_pb2.TakenAction(
                    who=who,
                    type=mahjong_pb2.ACTION_TYPE_DISCARD,
                    discard=discard,
                    discard_drawn_tile=discard_drawn_tile,
                )
            elif key == "N":
                who = int(val["who"])
                open = int(val["m"])
                taken_action = mahjong_pb2.TakenAction(
                    who=who,
                    type=MjlogParser._open_type(open),
                    open=open,
                )
                continue
            elif key == "REACH":
                if int(val["step"]) == 1:
                    who = int(val["who"])
                    taken_action = mahjong_pb2.TakenAction(
                        who=who,
                        type=mahjong_pb2.ACTION_TYPE_RIICHI
                    )
                else:
                    self.state.score.ten[:] = [int(x) for x in val["ten"].split(",")]
                    continue
            elif key == "DORA":
                dora = int(val["hai"])
                self.state.dora.append(dora)
                continue
            elif key == "RYUUKYOKU":
                self.state.end_info.scores_before[:] = [int(x) for i, x in enumerate(val["sc"].split(",")) if i % 2 == 0]
                self.state.end_info.score_changes[:] = [int(x) for i, x in enumerate(val["sc"].split(",")) if i % 2 == 1]
                self.state.end_info.scores_after[:] = [x + y for x, y in zip(self.state.end_info.scores_before, self.state.end_info.score_changes)]
                for i in range(4):
                    hai_key = "hai" + str(i)
                    if hai_key not in val:
                        continue
                    self.state.end_info.tenpais.append(mahjong_pb2.TenpaiHand(
                            who=i,
                            closed_tiles=[int(x) for x in val[hai_key].split(",")],
                    ))
                if "owari" in val:
                    self.state.end_info.is_game_over = True
            elif key == "AGARI":
                who = int(val["who"])
                from_who = int(val["fromWho"])
                # set taken_action
                taken_action = mahjong_pb2.TakenAction(
                    who=who,
                    type=mahjong_pb2.ACTION_TYPE_TSUMO if who == from_who else mahjong_pb2.ACTION_TYPE_RON
                )
                # set win info
                # TODO(sotetsuk): yakuman
                # TODO(sotetsuk): check double ron behavior
                self.state.end_info.scores_before[:] = [int(x) for i, x in enumerate(val["sc"].split(",")) if i % 2 == 0]
                self.state.end_info.score_changes[:] = [int(x) for i, x in enumerate(val["sc"].split(",")) if i % 2 == 1]
                self.state.end_info.scores_after[:] = [x + y for x, y in zip(self.state.end_info.scores_before, self.state.end_info.score_changes)]
                win = mahjong_pb2.Win(
                    who=who,
                    from_who=from_who,
                    tiles=[int(x) for x in val["hai"].split(",")],
                    win_tile=int(val["machi"])
                )
                if "m" in val:
                    win.opens[:] = [int(x) for x in val["m"].split(",")]
                win.dora[:] = [int(x) for x in val["doraHai"].split(",")]
                if "doraHaiUra" in val:
                    win.ura_dora[:] = [int(x) for x in val["doraHaiUra"].split(",")]
                win.fu, win.ten, _ = [int(x) for x in val["ten"].split(",")]
                win.yakus[:] = [int(x) for i, x in enumerate(val["yaku"].split(",")) if i % 2 == 0]
                win.fans[:] = [int(x) for i, x in enumerate(val["yaku"].split(",")) if i % 2 == 1]
                if "yakuman" in val:
                    win.yakumans[:] = [int(x) for i, x in enumerate(val["yakuman"].split(",")) if i % 2 == 0]
                self.state.end_info.wins.append(win)
                if "owari" in val:
                    self.state.end_info.is_game_over = True
            elif key == "BYE":  # 接続切れ
                pass
            elif key == "UN":  # 再接続
                pass
            else:
                raise KeyError(key)
            self.state.action_history.taken_actions.append(taken_action)
            # yield copy.deepcopy(self.state)

        yield copy.deepcopy(self.state)

    @staticmethod
    def _to_wind(wind_str: str) -> mahjong_pb2.Wind:
        assert (wind_str in ["T", "U", "V", "W", "D", "E", "F", "G"])
        if wind_str in ["T", "D"]:
            return mahjong_pb2.WIND_EAST
        elif wind_str in ["U", "E"]:
            return mahjong_pb2.WIND_SOUTH
        elif wind_str in ["V", "F"]:
            return mahjong_pb2.WIND_WEST
        elif wind_str in ["W", "G"]:
            return mahjong_pb2.WIND_NORTH

    @staticmethod
    def _open_type(bits: int) -> mahjong_pb2.ActionType:
        if 1 << 2 & bits:
            return mahjong_pb2.ACTION_TYPE_CHI
        elif 1 << 3 & bits:
            if 1 << 4 & bits:
                return mahjong_pb2.ACTION_TYPE_KAN_ADDED
            else:
                return mahjong_pb2.ACTION_TYPE_PON
        else:
            if mahjong_pb2.RelativePos(bits & 3) == mahjong_pb2.RELATIVE_POS_SELF:
                return mahjong_pb2.ACTION_TYPE_KAN_CLOSED
            else:
                return mahjong_pb2.ACTION_TYPE_KAN_OPENED


if __name__ == "__main__":
    out = subprocess.run(
        "docker run sotetsuk/twr:v0.0.1 /twr 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 3".split(),
        capture_output=True)
    print(out.stdout.decode('utf-8'))
    parser = MjlogParser()
    for state in parser.parse("resources/2011020417gm-00a9-0000-b67fcaa3.mjlog"):
        print(json.dumps(json_format.MessageToDict(state, including_default_value_fields=False)))
