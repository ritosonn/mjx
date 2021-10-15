"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class ActionType(_ActionType, metaclass=_ActionTypeEnumTypeWrapper):
    pass
class _ActionType:
    V = typing.NewType('V', builtins.int)
class _ActionTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ActionType.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    ACTION_TYPE_DISCARD = ActionType.V(0)
    """After draw"""

    ACTION_TYPE_TSUMOGIRI = ActionType.V(1)
    ACTION_TYPE_RIICHI = ActionType.V(2)
    ACTION_TYPE_CLOSED_KAN = ActionType.V(3)
    ACTION_TYPE_ADDED_KAN = ActionType.V(4)
    ACTION_TYPE_TSUMO = ActionType.V(5)
    ACTION_TYPE_ABORTIVE_DRAW_NINE_TERMINALS = ActionType.V(6)
    """九種九牌"""

    ACTION_TYPE_CHI = ActionType.V(7)
    """After other's discard"""

    ACTION_TYPE_PON = ActionType.V(8)
    ACTION_TYPE_OPEN_KAN = ActionType.V(9)
    ACTION_TYPE_RON = ActionType.V(10)
    ACTION_TYPE_NO = ActionType.V(11)
    ACTION_TYPE_DUMMY = ActionType.V(99)
    """Dummy used only to check connection and share round terminal information"""


ACTION_TYPE_DISCARD = ActionType.V(0)
"""After draw"""

ACTION_TYPE_TSUMOGIRI = ActionType.V(1)
ACTION_TYPE_RIICHI = ActionType.V(2)
ACTION_TYPE_CLOSED_KAN = ActionType.V(3)
ACTION_TYPE_ADDED_KAN = ActionType.V(4)
ACTION_TYPE_TSUMO = ActionType.V(5)
ACTION_TYPE_ABORTIVE_DRAW_NINE_TERMINALS = ActionType.V(6)
"""九種九牌"""

ACTION_TYPE_CHI = ActionType.V(7)
"""After other's discard"""

ACTION_TYPE_PON = ActionType.V(8)
ACTION_TYPE_OPEN_KAN = ActionType.V(9)
ACTION_TYPE_RON = ActionType.V(10)
ACTION_TYPE_NO = ActionType.V(11)
ACTION_TYPE_DUMMY = ActionType.V(99)
"""Dummy used only to check connection and share round terminal information"""

global___ActionType = ActionType


class EventType(_EventType, metaclass=_EventTypeEnumTypeWrapper):
    pass
class _EventType:
    V = typing.NewType('V', builtins.int)
class _EventTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_EventType.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    EVENT_TYPE_DISCARD = EventType.V(0)
    """Publicly observable actions"""

    EVENT_TYPE_TSUMOGIRI = EventType.V(1)
    """ツモ切り, Tsumogiri"""

    EVENT_TYPE_RIICHI = EventType.V(2)
    EVENT_TYPE_CLOSED_KAN = EventType.V(3)
    EVENT_TYPE_ADDED_KAN = EventType.V(4)
    EVENT_TYPE_TSUMO = EventType.V(5)
    EVENT_TYPE_ABORTIVE_DRAW_NINE_TERMINALS = EventType.V(6)
    EVENT_TYPE_CHI = EventType.V(7)
    EVENT_TYPE_PON = EventType.V(8)
    EVENT_TYPE_OPEN_KAN = EventType.V(9)
    EVENT_TYPE_RON = EventType.V(10)
    EVENT_TYPE_DRAW = EventType.V(12)
    """State transitions made by environment. There is no decision making by players.
    11 is skipped for the consistency to ActionType
    """

    EVENT_TYPE_RIICHI_SCORE_CHANGE = EventType.V(13)
    EVENT_TYPE_NEW_DORA = EventType.V(14)
    EVENT_TYPE_ABORTIVE_DRAW_FOUR_RIICHIS = EventType.V(15)
    """四家立直"""

    EVENT_TYPE_ABORTIVE_DRAW_THREE_RONS = EventType.V(16)
    """三家和了"""

    EVENT_TYPE_ABORTIVE_DRAW_FOUR_KANS = EventType.V(17)
    """四槓散了"""

    EVENT_TYPE_ABORTIVE_DRAW_FOUR_WINDS = EventType.V(18)
    """四風連打"""

    EVENT_TYPE_EXHAUSTIVE_DRAW_NORMAL = EventType.V(19)
    """通常流局"""

    EVENT_TYPE_EXHAUSTIVE_DRAW_NAGASHI_MANGAN = EventType.V(20)
    """流し満貫"""


EVENT_TYPE_DISCARD = EventType.V(0)
"""Publicly observable actions"""

EVENT_TYPE_TSUMOGIRI = EventType.V(1)
"""ツモ切り, Tsumogiri"""

EVENT_TYPE_RIICHI = EventType.V(2)
EVENT_TYPE_CLOSED_KAN = EventType.V(3)
EVENT_TYPE_ADDED_KAN = EventType.V(4)
EVENT_TYPE_TSUMO = EventType.V(5)
EVENT_TYPE_ABORTIVE_DRAW_NINE_TERMINALS = EventType.V(6)
EVENT_TYPE_CHI = EventType.V(7)
EVENT_TYPE_PON = EventType.V(8)
EVENT_TYPE_OPEN_KAN = EventType.V(9)
EVENT_TYPE_RON = EventType.V(10)
EVENT_TYPE_DRAW = EventType.V(12)
"""State transitions made by environment. There is no decision making by players.
11 is skipped for the consistency to ActionType
"""

EVENT_TYPE_RIICHI_SCORE_CHANGE = EventType.V(13)
EVENT_TYPE_NEW_DORA = EventType.V(14)
EVENT_TYPE_ABORTIVE_DRAW_FOUR_RIICHIS = EventType.V(15)
"""四家立直"""

EVENT_TYPE_ABORTIVE_DRAW_THREE_RONS = EventType.V(16)
"""三家和了"""

EVENT_TYPE_ABORTIVE_DRAW_FOUR_KANS = EventType.V(17)
"""四槓散了"""

EVENT_TYPE_ABORTIVE_DRAW_FOUR_WINDS = EventType.V(18)
"""四風連打"""

EVENT_TYPE_EXHAUSTIVE_DRAW_NORMAL = EventType.V(19)
"""通常流局"""

EVENT_TYPE_EXHAUSTIVE_DRAW_NAGASHI_MANGAN = EventType.V(20)
"""流し満貫"""

global___EventType = EventType


class Score(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ROUND_FIELD_NUMBER: builtins.int
    HONBA_FIELD_NUMBER: builtins.int
    RIICHI_FIELD_NUMBER: builtins.int
    TENS_FIELD_NUMBER: builtins.int
    round: builtins.int = ...
    honba: builtins.int = ...
    riichi: builtins.int = ...
    """For final score, riichi = 0 if someone wins (or at the end of game)"""

    @property
    def tens(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """Following rule holds for all rounds: sum(score.ten) + score.riichi * 1000 == 100000"""
        pass
    def __init__(self,
        *,
        round : builtins.int = ...,
        honba : builtins.int = ...,
        riichi : builtins.int = ...,
        tens : typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["honba",b"honba","riichi",b"riichi","round",b"round","tens",b"tens"]) -> None: ...
global___Score = Score

class Event(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TYPE_FIELD_NUMBER: builtins.int
    WHO_FIELD_NUMBER: builtins.int
    TILE_FIELD_NUMBER: builtins.int
    OPEN_FIELD_NUMBER: builtins.int
    type: global___EventType.V = ...
    """Publicly observable event, which include

      1. publicly observable and actually realized actions taken by all layers
      2. publicly observable state transitions made by envionment

    Note that "No" action is **NOT** collected as event since it's not publicly observable.
    Also, "Chi" prevented by other player's "Pon/Ron" is also **NOT** collected in event_history.
    Drawn tile does not use tile entry because it's not publicly observable.
    Only the fact that the player drew something is collected.

    Table. Is who/tile/open entry set?
                                       who    tile    open
     0. DISCARD                        Yes     Yes      No
     1. TSUMOGIRI                      Yes     Yes      No
     2. RIICHI                         Yes      No      No
     3. CLOSED_KAN                     Yes      No     Yes
     4. ADDED_KAN                      Yes      No     Yes
     5. TSUMO                          Yes     Yes      No
     6. ABORTIVE_DRAW_NINE_TERMINALS   Yes      No      No
     7. CHI                            Yes      No     Yes
     8. PON                            Yes      No     Yes
     9. OPEN_KAN                       Yes      No     Yes
    10. RON                            Yes     Yes      No
    12. DRAW                           Yes      No      No
    13. RIICHI_SCORE_CHANGE            Yes      No      No
    14. NEW_DORA                        No     Yes      No
    15. ABORTIVE_DRAW_FOUR_RIICHIS      No      No      No
    16. ABORTIVE_DRAW_THREE_RONS        No      No      No
    17. ABORTIVE_DRAW_FOUR_KANS         No      No      No
    18. ABORTIVE_DRAW_FOUR_WINDS        No      No      No
    19. EXHAUSTIVE_DRAW_NORMAL          No      No      No
    20. EXHAUSTIVE_DRAW_NAGASHI_MANGAN  No      No      No
    """

    who: builtins.int = ...
    tile: builtins.int = ...
    open: builtins.int = ...
    def __init__(self,
        *,
        type : global___EventType.V = ...,
        who : builtins.int = ...,
        tile : builtins.int = ...,
        open : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["open",b"open","tile",b"tile","type",b"type","who",b"who"]) -> None: ...
global___Event = Event

class PublicObservation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    GAME_ID_FIELD_NUMBER: builtins.int
    PLAYER_IDS_FIELD_NUMBER: builtins.int
    INIT_SCORE_FIELD_NUMBER: builtins.int
    DORA_INDICATORS_FIELD_NUMBER: builtins.int
    EVENTS_FIELD_NUMBER: builtins.int
    game_id: typing.Text = ...
    @property
    def player_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Sorted by the dealer order (起家, ..., ラス親)"""
        pass
    @property
    def init_score(self) -> global___Score:
        """public info"""
        pass
    @property
    def dora_indicators(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """len(dora_indicators) = 1 + # of Kan"""
        pass
    @property
    def events(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Event]: ...
    def __init__(self,
        *,
        game_id : typing.Text = ...,
        player_ids : typing.Optional[typing.Iterable[typing.Text]] = ...,
        init_score : typing.Optional[global___Score] = ...,
        dora_indicators : typing.Optional[typing.Iterable[builtins.int]] = ...,
        events : typing.Optional[typing.Iterable[global___Event]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["init_score",b"init_score"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dora_indicators",b"dora_indicators","events",b"events","game_id",b"game_id","init_score",b"init_score","player_ids",b"player_ids"]) -> None: ...
global___PublicObservation = PublicObservation

class Hand(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CLOSED_TILES_FIELD_NUMBER: builtins.int
    OPENS_FIELD_NUMBER: builtins.int
    @property
    def closed_tiles(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    @property
    def opens(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """[1st open, 2nd open, ...]"""
        pass
    def __init__(self,
        *,
        closed_tiles : typing.Optional[typing.Iterable[builtins.int]] = ...,
        opens : typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["closed_tiles",b"closed_tiles","opens",b"opens"]) -> None: ...
global___Hand = Hand

class PrivateObservation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    WHO_FIELD_NUMBER: builtins.int
    INIT_HAND_FIELD_NUMBER: builtins.int
    DRAW_HISTORY_FIELD_NUMBER: builtins.int
    CURR_HAND_FIELD_NUMBER: builtins.int
    who: builtins.int = ...
    @property
    def init_hand(self) -> global___Hand: ...
    @property
    def draw_history(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    @property
    def curr_hand(self) -> global___Hand: ...
    def __init__(self,
        *,
        who : builtins.int = ...,
        init_hand : typing.Optional[global___Hand] = ...,
        draw_history : typing.Optional[typing.Iterable[builtins.int]] = ...,
        curr_hand : typing.Optional[global___Hand] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["curr_hand",b"curr_hand","init_hand",b"init_hand"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["curr_hand",b"curr_hand","draw_history",b"draw_history","init_hand",b"init_hand","who",b"who"]) -> None: ...
global___PrivateObservation = PrivateObservation

class Observation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    WHO_FIELD_NUMBER: builtins.int
    PUBLIC_OBSERVATION_FIELD_NUMBER: builtins.int
    PRIVATE_OBSERVATION_FIELD_NUMBER: builtins.int
    ROUND_TERMINAL_FIELD_NUMBER: builtins.int
    LEGAL_ACTIONS_FIELD_NUMBER: builtins.int
    who: builtins.int = ...
    @property
    def public_observation(self) -> global___PublicObservation: ...
    @property
    def private_observation(self) -> global___PrivateObservation: ...
    @property
    def round_terminal(self) -> global___RoundTerminal: ...
    @property
    def legal_actions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Action]: ...
    def __init__(self,
        *,
        who : builtins.int = ...,
        public_observation : typing.Optional[global___PublicObservation] = ...,
        private_observation : typing.Optional[global___PrivateObservation] = ...,
        round_terminal : typing.Optional[global___RoundTerminal] = ...,
        legal_actions : typing.Optional[typing.Iterable[global___Action]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["private_observation",b"private_observation","public_observation",b"public_observation","round_terminal",b"round_terminal"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["legal_actions",b"legal_actions","private_observation",b"private_observation","public_observation",b"public_observation","round_terminal",b"round_terminal","who",b"who"]) -> None: ...
global___Observation = Observation

class Win(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    WHO_FIELD_NUMBER: builtins.int
    FROM_WHO_FIELD_NUMBER: builtins.int
    HAND_FIELD_NUMBER: builtins.int
    WIN_TILE_FIELD_NUMBER: builtins.int
    FU_FIELD_NUMBER: builtins.int
    TEN_FIELD_NUMBER: builtins.int
    TEN_CHANGES_FIELD_NUMBER: builtins.int
    YAKUS_FIELD_NUMBER: builtins.int
    FANS_FIELD_NUMBER: builtins.int
    YAKUMANS_FIELD_NUMBER: builtins.int
    URA_DORA_INDICATORS_FIELD_NUMBER: builtins.int
    who: builtins.int = ...
    from_who: builtins.int = ...
    @property
    def hand(self) -> global___Hand: ...
    win_tile: builtins.int = ...
    fu: builtins.int = ...
    ten: builtins.int = ...
    @property
    def ten_changes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """Required for Tenhou mjlog."""
        pass
    @property
    def yakus(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    @property
    def fans(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    @property
    def yakumans(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    @property
    def ura_dora_indicators(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """set if this player is under riichi"""
        pass
    def __init__(self,
        *,
        who : builtins.int = ...,
        from_who : builtins.int = ...,
        hand : typing.Optional[global___Hand] = ...,
        win_tile : builtins.int = ...,
        fu : builtins.int = ...,
        ten : builtins.int = ...,
        ten_changes : typing.Optional[typing.Iterable[builtins.int]] = ...,
        yakus : typing.Optional[typing.Iterable[builtins.int]] = ...,
        fans : typing.Optional[typing.Iterable[builtins.int]] = ...,
        yakumans : typing.Optional[typing.Iterable[builtins.int]] = ...,
        ura_dora_indicators : typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["hand",b"hand"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["fans",b"fans","from_who",b"from_who","fu",b"fu","hand",b"hand","ten",b"ten","ten_changes",b"ten_changes","ura_dora_indicators",b"ura_dora_indicators","who",b"who","win_tile",b"win_tile","yakumans",b"yakumans","yakus",b"yakus"]) -> None: ...
global___Win = Win

class NoWinner(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TENPAIS_FIELD_NUMBER: builtins.int
    TEN_CHANGES_FIELD_NUMBER: builtins.int
    @property
    def tenpais(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TenpaiHand]: ...
    @property
    def ten_changes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """Required for Tenhou mjlog."""
        pass
    def __init__(self,
        *,
        tenpais : typing.Optional[typing.Iterable[global___TenpaiHand]] = ...,
        ten_changes : typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ten_changes",b"ten_changes","tenpais",b"tenpais"]) -> None: ...
global___NoWinner = NoWinner

class TenpaiHand(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    WHO_FIELD_NUMBER: builtins.int
    HAND_FIELD_NUMBER: builtins.int
    who: builtins.int = ...
    @property
    def hand(self) -> global___Hand: ...
    def __init__(self,
        *,
        who : builtins.int = ...,
        hand : typing.Optional[global___Hand] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["hand",b"hand"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["hand",b"hand","who",b"who"]) -> None: ...
global___TenpaiHand = TenpaiHand

class RoundTerminal(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FINAL_SCORE_FIELD_NUMBER: builtins.int
    WINS_FIELD_NUMBER: builtins.int
    NO_WINNER_FIELD_NUMBER: builtins.int
    IS_GAME_OVER_FIELD_NUMBER: builtins.int
    @property
    def final_score(self) -> global___Score: ...
    @property
    def wins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Win]:
        """Empty if no one wins"""
        pass
    @property
    def no_winner(self) -> global___NoWinner:
        """Empty if a winner exists"""
        pass
    is_game_over: builtins.bool = ...
    def __init__(self,
        *,
        final_score : typing.Optional[global___Score] = ...,
        wins : typing.Optional[typing.Iterable[global___Win]] = ...,
        no_winner : typing.Optional[global___NoWinner] = ...,
        is_game_over : builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["final_score",b"final_score","no_winner",b"no_winner"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["final_score",b"final_score","is_game_over",b"is_game_over","no_winner",b"no_winner","wins",b"wins"]) -> None: ...
global___RoundTerminal = RoundTerminal

class State(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    HIDDEN_STATE_FIELD_NUMBER: builtins.int
    PUBLIC_OBSERVATION_FIELD_NUMBER: builtins.int
    PRIVATE_OBSERVATIONS_FIELD_NUMBER: builtins.int
    ROUND_TERMINAL_FIELD_NUMBER: builtins.int
    @property
    def hidden_state(self) -> global___HiddenState: ...
    @property
    def public_observation(self) -> global___PublicObservation: ...
    @property
    def private_observations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PrivateObservation]: ...
    @property
    def round_terminal(self) -> global___RoundTerminal: ...
    def __init__(self,
        *,
        hidden_state : typing.Optional[global___HiddenState] = ...,
        public_observation : typing.Optional[global___PublicObservation] = ...,
        private_observations : typing.Optional[typing.Iterable[global___PrivateObservation]] = ...,
        round_terminal : typing.Optional[global___RoundTerminal] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["hidden_state",b"hidden_state","public_observation",b"public_observation","round_terminal",b"round_terminal"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["hidden_state",b"hidden_state","private_observations",b"private_observations","public_observation",b"public_observation","round_terminal",b"round_terminal"]) -> None: ...
global___State = State

class HiddenState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    GAME_SEED_FIELD_NUMBER: builtins.int
    WALL_FIELD_NUMBER: builtins.int
    URA_DORA_INDICATORS_FIELD_NUMBER: builtins.int
    game_seed: builtins.int = ...
    @property
    def wall(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    @property
    def ura_dora_indicators(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """len(ura_dora_indicators) = 1 + # of Kan"""
        pass
    def __init__(self,
        *,
        game_seed : builtins.int = ...,
        wall : typing.Optional[typing.Iterable[builtins.int]] = ...,
        ura_dora_indicators : typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["game_seed",b"game_seed","ura_dora_indicators",b"ura_dora_indicators","wall",b"wall"]) -> None: ...
global___HiddenState = HiddenState

class Action(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    GAME_ID_FIELD_NUMBER: builtins.int
    WHO_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    TILE_FIELD_NUMBER: builtins.int
    OPEN_FIELD_NUMBER: builtins.int
    game_id: typing.Text = ...
    """                  tile   open
     DISCARD           Yes     No
     TSUMOGIRI         Yes     No
     RIICHI             No     No
     TSUMO             Yes     No
     CLOSED_KAN         No    Yes
     ADDED_KAN          No    Yes
     KYUSYU             No     No
     NO                 No     No
     CHI                No    Yes
     PON                No    Yes
     OPEN_KAN           No    Yes
     RON                Yes    No
    """

    who: builtins.int = ...
    type: global___ActionType.V = ...
    tile: builtins.int = ...
    open: builtins.int = ...
    def __init__(self,
        *,
        game_id : typing.Text = ...,
        who : builtins.int = ...,
        type : global___ActionType.V = ...,
        tile : builtins.int = ...,
        open : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["game_id",b"game_id","open",b"open","tile",b"tile","type",b"type","who",b"who"]) -> None: ...
global___Action = Action

class GameResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class TensEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: builtins.int = ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : builtins.int = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    class RankingsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: builtins.int = ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : builtins.int = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    GAME_SEED_FIELD_NUMBER: builtins.int
    PLAYER_IDS_FIELD_NUMBER: builtins.int
    TENS_FIELD_NUMBER: builtins.int
    RANKINGS_FIELD_NUMBER: builtins.int
    game_seed: builtins.int = ...
    @property
    def player_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Sorted by the dealer order (起家, ..., ラス親)"""
        pass
    @property
    def tens(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, builtins.int]: ...
    @property
    def rankings(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, builtins.int]:
        """ranking in {1, 2, 3, 4}"""
        pass
    def __init__(self,
        *,
        game_seed : builtins.int = ...,
        player_ids : typing.Optional[typing.Iterable[typing.Text]] = ...,
        tens : typing.Optional[typing.Mapping[typing.Text, builtins.int]] = ...,
        rankings : typing.Optional[typing.Mapping[typing.Text, builtins.int]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["game_seed",b"game_seed","player_ids",b"player_ids","rankings",b"rankings","tens",b"tens"]) -> None: ...
global___GameResult = GameResult
