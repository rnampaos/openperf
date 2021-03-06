#ifndef _OP_PACKETIO_JSON_TRANSMOGRIFY_HPP_
#define _OP_PACKETIO_JSON_TRANSMOGRIFY_HPP_

#include "json.hpp"
#include "swagger/v1/model/Interface.h"
#include "swagger/v1/model/Port.h"

namespace swagger {
namespace v1 {
namespace model {

void from_json(const nlohmann::json&, swagger::v1::model::Interface&);
void from_json(const nlohmann::json&, swagger::v1::model::Port&);

} // namespace model
} // namespace v1
} // namespace swagger

namespace openperf {
namespace packetio {
static const std::string empty_id_string = "none";
}
} // namespace openperf

#endif /* _OP_PACKETIO_JSON_TRANSMOGRIFY_HPP_ */
