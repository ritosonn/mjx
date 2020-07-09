#ifndef MAHJONG_WIN_SCORE_H
#define MAHJONG_WIN_SCORE_H

#include "types.h"
#include <map>
#include <utility>

namespace mj {

    class WinningScore {
    private:
        std::map<Yaku,int> yaku_;
        std::map<Yaku,bool> yakuman_;
        std::optional<int> fu_;
    public:
        [[nodiscard]] const std::map<Yaku,int>& yaku() const noexcept ;
        [[nodiscard]] const std::map<Yaku,bool>& yakuman() const noexcept ;
        [[nodiscard]] std::optional<int> fu() const noexcept ;
        [[nodiscard]] std::optional<int> HasYaku(Yaku yaku) const noexcept ;
        [[nodiscard]] bool HasYakuman(Yaku yakuman) const noexcept ;
        void AddYaku(Yaku yaku, int fan) noexcept ;
        void AddYakuman(Yaku yaku) noexcept ;
        void SetFu(int fu) noexcept ;
        [[nodiscard]] bool RequireFan() const noexcept ;
        [[nodiscard]] bool RequireFu() const noexcept ;
    };

} // namespace mj

#endif //MAHJONG_WIN_SCORE_H
