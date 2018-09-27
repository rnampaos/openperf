/**
* Inception Core API
* REST API interface to the Inception Core
*
* OpenAPI spec version: 1
* Contact: support@spirent.com
*
* NOTE: This class is auto generated by the swagger code generator program.
* https://github.com/swagger-api/swagger-codegen.git
* Do not edit the class manually.
*/


#include "StackProtocolStats.h"

namespace swagger {
namespace v1 {
namespace model {

StackProtocolStats::StackProtocolStats()
{
    m_Tx_packets = 0L;
    m_Rx_packets = 0L;
    m_Forwarded_packets = 0L;
    m_Dropped_packets = 0L;
    m_Checksum_errors = 0L;
    m_Length_errors = 0L;
    m_Memory_errors = 0L;
    m_Routing_errors = 0L;
    m_Protocol_errors = 0L;
    m_Option_errors = 0L;
    m_Misc_errors = 0L;
    m_Cache_hits = 0L;
    
}

StackProtocolStats::~StackProtocolStats()
{
}

void StackProtocolStats::validate()
{
    // TODO: implement validation
}

nlohmann::json StackProtocolStats::toJson() const
{
    nlohmann::json val = nlohmann::json::object();

    val["tx_packets"] = m_Tx_packets;
    val["rx_packets"] = m_Rx_packets;
    val["forwarded_packets"] = m_Forwarded_packets;
    val["dropped_packets"] = m_Dropped_packets;
    val["checksum_errors"] = m_Checksum_errors;
    val["length_errors"] = m_Length_errors;
    val["memory_errors"] = m_Memory_errors;
    val["routing_errors"] = m_Routing_errors;
    val["protocol_errors"] = m_Protocol_errors;
    val["option_errors"] = m_Option_errors;
    val["misc_errors"] = m_Misc_errors;
    val["cache_hits"] = m_Cache_hits;
    

    return val;
}

void StackProtocolStats::fromJson(nlohmann::json& val)
{
    setTxPackets(val.at("tx_packets"));
    setRxPackets(val.at("rx_packets"));
    setForwardedPackets(val.at("forwarded_packets"));
    setDroppedPackets(val.at("dropped_packets"));
    setChecksumErrors(val.at("checksum_errors"));
    setLengthErrors(val.at("length_errors"));
    setMemoryErrors(val.at("memory_errors"));
    setRoutingErrors(val.at("routing_errors"));
    setProtocolErrors(val.at("protocol_errors"));
    setOptionErrors(val.at("option_errors"));
    setMiscErrors(val.at("misc_errors"));
    setCacheHits(val.at("cache_hits"));
    
}


int64_t StackProtocolStats::getTxPackets() const
{
    return m_Tx_packets;
}
void StackProtocolStats::setTxPackets(int64_t value)
{
    m_Tx_packets = value;
    
}
int64_t StackProtocolStats::getRxPackets() const
{
    return m_Rx_packets;
}
void StackProtocolStats::setRxPackets(int64_t value)
{
    m_Rx_packets = value;
    
}
int64_t StackProtocolStats::getForwardedPackets() const
{
    return m_Forwarded_packets;
}
void StackProtocolStats::setForwardedPackets(int64_t value)
{
    m_Forwarded_packets = value;
    
}
int64_t StackProtocolStats::getDroppedPackets() const
{
    return m_Dropped_packets;
}
void StackProtocolStats::setDroppedPackets(int64_t value)
{
    m_Dropped_packets = value;
    
}
int64_t StackProtocolStats::getChecksumErrors() const
{
    return m_Checksum_errors;
}
void StackProtocolStats::setChecksumErrors(int64_t value)
{
    m_Checksum_errors = value;
    
}
int64_t StackProtocolStats::getLengthErrors() const
{
    return m_Length_errors;
}
void StackProtocolStats::setLengthErrors(int64_t value)
{
    m_Length_errors = value;
    
}
int64_t StackProtocolStats::getMemoryErrors() const
{
    return m_Memory_errors;
}
void StackProtocolStats::setMemoryErrors(int64_t value)
{
    m_Memory_errors = value;
    
}
int64_t StackProtocolStats::getRoutingErrors() const
{
    return m_Routing_errors;
}
void StackProtocolStats::setRoutingErrors(int64_t value)
{
    m_Routing_errors = value;
    
}
int64_t StackProtocolStats::getProtocolErrors() const
{
    return m_Protocol_errors;
}
void StackProtocolStats::setProtocolErrors(int64_t value)
{
    m_Protocol_errors = value;
    
}
int64_t StackProtocolStats::getOptionErrors() const
{
    return m_Option_errors;
}
void StackProtocolStats::setOptionErrors(int64_t value)
{
    m_Option_errors = value;
    
}
int64_t StackProtocolStats::getMiscErrors() const
{
    return m_Misc_errors;
}
void StackProtocolStats::setMiscErrors(int64_t value)
{
    m_Misc_errors = value;
    
}
int64_t StackProtocolStats::getCacheHits() const
{
    return m_Cache_hits;
}
void StackProtocolStats::setCacheHits(int64_t value)
{
    m_Cache_hits = value;
    
}

}
}
}
