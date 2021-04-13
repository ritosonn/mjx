#ifndef MAHJONG_OBSERVATION_H
#define MAHJONG_OBSERVATION_H

#include <array>
#include <utility>

#include "action.h"
#include "hand.h"
#include "mjx.pb.h"

namespace mjx::internal {
class Observation {
 public:
  Observation() = default;
  Observation(const mjxproto::Observation& proto);
  Observation(AbsolutePos who, const mjxproto::State& state);

  AbsolutePos who() const;
  [[nodiscard]] bool has_possible_action() const;
  [[nodiscard]] std::vector<mjxproto::Action> possible_actions() const;
  [[nodiscard]] std::vector<Tile> possible_discards() const;
  Hand initial_hand() const;
  Hand current_hand() const;
  std::string ToJson() const;
  const mjxproto::Observation& proto() const;
  [[nodiscard]] std::vector<mjxproto::Event> EventHistory() const;

  void add_possible_action(mjxproto::Action&& possible_action);
  void add_possible_actions(
      const std::vector<mjxproto::Action>& possible_actions);

 private:
  // TODO: remove friends and use proto()
  friend class State;
  mjxproto::Observation proto_ = mjxproto::Observation{};
};
}  // namespace mjx::internal

#endif  // MAHJONG_OBSERVATION_H