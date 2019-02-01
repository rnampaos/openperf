#ifndef _ICP_SOCKET_CLIENT_IO_CHANNEL_WRAPPER_H_
#define _ICP_SOCKET_CLIENT_IO_CHANNEL_WRAPPER_H_

#include "tl/expected.hpp"

#include "socket/api.h"
#include "socket/client/dgram_channel.h"
#include "socket/client/stream_channel.h"

namespace icp {
namespace socket {
namespace client {

class io_channel_wrapper
{
    using io_channel = std::variant<icp::socket::client::dgram_channel*,
                                    icp::socket::client::stream_channel*>;
    io_channel m_channel;

    static io_channel to_io_channel(api::io_channel&);

public:
    io_channel_wrapper(api::io_channel& channel, int client_fd, int server_fd);
    ~io_channel_wrapper();

    io_channel_wrapper(const io_channel_wrapper&) = delete;
    io_channel_wrapper& operator=(const io_channel_wrapper&&) = delete;

    io_channel_wrapper(io_channel_wrapper&&);
    io_channel_wrapper& operator=(io_channel_wrapper&&);

    int flags();
    int flags(int);

    tl::expected<size_t, int> send(pid_t pid, const iovec iov[], size_t iovcnt,
                                   const sockaddr *to);

    tl::expected<size_t, int> recv(pid_t pid, iovec iov[], size_t iovcnt,
                                   sockaddr *from, socklen_t *fromlen);

    int recv_clear();
};

}
}
}

#endif /* _ICP_SOCKET_CLIENT_IO_CHANNEL_WRAPPER_H_ */