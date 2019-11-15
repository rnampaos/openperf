#ifndef _ICP_PACKETIO_INTERNAL_CLIENT_H_
#define _ICP_PACKETIO_INTERNAL_CLIENT_H_

#include <any>
#include <memory>
#include "tl/expected.hpp"

#include "core/icp_core.h"
#include "packetio/generic_event_loop.h"
#include "packetio/generic_sink.h"
#include "packetio/generic_source.h"
#include "packetio/generic_workers.h"

namespace icp::packetio::internal::api {

class client
{
    std::unique_ptr<void, icp_socket_deleter> m_socket;

    tl::expected<std::string, int> add_task_impl(workers::context ctx,
                                                 std::string_view name,
                                                 event_loop::event_notifier notify,
                                                 event_loop::event_handler on_event,
                                                 std::optional<event_loop::delete_handler> on_delete,
                                                 std::any arg);
public:
    client(void* context);

    client(client&& other);
    client& operator=(client&& other);

    tl::expected<std::vector<unsigned>, int>
    get_worker_rx_ids(std::optional<std::string_view> obj_id = std::nullopt);
    tl::expected<std::vector<unsigned>, int>
    get_worker_tx_ids(std::optional<std::string_view> obj_id = std::nullopt);

    tl::expected<void, int> add_sink(std::string_view src_id,
                                     packets::generic_sink sink);
    tl::expected<void, int> del_sink(std::string_view src_id,
                                     packets::generic_sink sink);
    tl::expected<void, int> add_source(std::string_view dst_id,
                                       packets::generic_source source);
    tl::expected<void, int> del_source(std::string_view dst_id,
                                       packets::generic_source source);

    tl::expected<std::string, int> add_task(workers::context ctx,
                                            std::string_view name,
                                            event_loop::event_notifier notify,
                                            event_loop::event_handler on_event,
                                            std::any arg);

    tl::expected<std::string, int> add_task(workers::context ctx,
                                            std::string_view name,
                                            event_loop::event_notifier notify,
                                            event_loop::event_handler on_event,
                                            event_loop::delete_handler on_delete,
                                            std::any arg);

    tl::expected<void, int> del_task(std::string_view task_id);
};

}

#endif /* _ICP_PACKETIO_INTERNAL_CLIENT_H_ */
