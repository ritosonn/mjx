#ifndef MJX_PROJECT_HAND_H
#define MJX_PROJECT_HAND_H

#include "mjx/internal/mjx.grpc.pb.h"

namespace mjx {
class Hand {
 public:
  Hand() = default;
  explicit Hand(mjxproto::Hand proto);
  explicit Hand(const std::string& json);
  const mjxproto::Hand& ToProto() const noexcept;
  std::string ToJson() const noexcept;
  bool operator==(const Hand& other) const noexcept;
  bool operator!=(const Hand& other) const noexcept;

 private:
  mjxproto::Hand proto_{};
};
}  // namespace mjx

#endif  // MJX_PROJECT_HAND_H