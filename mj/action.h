#ifndef MAHJONG_ACTION_H
#define MAHJONG_ACTION_H

#include <memory>
#include <utility>
#include "mj.pb.h"
#include "types.h"
#include "tile.h"
#include "open.h"

namespace mj
{
    class Action
    {
    public:
        Action() = delete;
        static bool IsValid(const mjproto::Action &action);
        static mjproto::Action CreateDiscard(AbsolutePos who, Tile discard);
        static std::vector<mjproto::Action> CreateDiscards(AbsolutePos who, const std::vector<Tile>& discards);
        static mjproto::Action CreateRiichi(AbsolutePos who);
        static mjproto::Action CreateTsumo(AbsolutePos who);
        static mjproto::Action CreateRon(AbsolutePos who);
        static mjproto::Action CreateOpen(AbsolutePos who, Open open);
        static mjproto::Action CreateNo(AbsolutePos who);
        static mjproto::Action CreateNineTiles(AbsolutePos who);
    };
}  // namespace mj

#endif //MAHJONG_ACTION_H
