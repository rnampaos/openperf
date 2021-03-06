/**
* OpenPerf API
* REST API interface for OpenPerf
*
* OpenAPI spec version: 1
* Contact: support@spirent.com
*
* NOTE: This class is auto generated by the swagger code generator program.
* https://github.com/swagger-api/swagger-codegen.git
* Do not edit the class manually.
*/


#include "StackStats.h"

namespace swagger {
namespace v1 {
namespace model {

StackStats::StackStats()
{
    
}

StackStats::~StackStats()
{
}

void StackStats::validate()
{
    // TODO: implement validation
}

nlohmann::json StackStats::toJson() const
{
    nlohmann::json val = nlohmann::json::object();

    val["arp"] = ModelBase::toJson(m_Arp);
    val["ipv4"] = ModelBase::toJson(m_Ipv4);
    val["ipv4_frag"] = ModelBase::toJson(m_Ipv4_frag);
    val["icmpv4"] = ModelBase::toJson(m_Icmpv4);
    val["igmp"] = ModelBase::toJson(m_Igmp);
    val["nd"] = ModelBase::toJson(m_Nd);
    val["ipv6"] = ModelBase::toJson(m_Ipv6);
    val["ipv6_frag"] = ModelBase::toJson(m_Ipv6_frag);
    val["icmpv6"] = ModelBase::toJson(m_Icmpv6);
    val["mld"] = ModelBase::toJson(m_Mld);
    val["udp"] = ModelBase::toJson(m_Udp);
    val["tcp"] = ModelBase::toJson(m_Tcp);
    val["heap"] = ModelBase::toJson(m_Heap);
    {
        nlohmann::json jsonArray;
        for( auto& item : m_Pools )
        {
            jsonArray.push_back(ModelBase::toJson(item));
        }
        val["pools"] = jsonArray;
            }
    val["sems"] = ModelBase::toJson(m_Sems);
    val["mutexes"] = ModelBase::toJson(m_Mutexes);
    val["mboxes"] = ModelBase::toJson(m_Mboxes);
    

    return val;
}

void StackStats::fromJson(nlohmann::json& val)
{
    {
        m_Pools.clear();
        nlohmann::json jsonArray;
                for( auto& item : val["pools"] )
        {
            
            if(item.is_null())
            {
                m_Pools.push_back( std::shared_ptr<StackMemoryStats>(nullptr) );
            }
            else
            {
                std::shared_ptr<StackMemoryStats> newItem(new StackMemoryStats());
                newItem->fromJson(item);
                m_Pools.push_back( newItem );
            }
            
        }
    }
    
}


std::shared_ptr<StackProtocolStats> StackStats::getArp() const
{
    return m_Arp;
}
void StackStats::setArp(std::shared_ptr<StackProtocolStats> value)
{
    m_Arp = value;
    
}
std::shared_ptr<StackProtocolStats> StackStats::getIpv4() const
{
    return m_Ipv4;
}
void StackStats::setIpv4(std::shared_ptr<StackProtocolStats> value)
{
    m_Ipv4 = value;
    
}
std::shared_ptr<StackProtocolStats> StackStats::getIpv4Frag() const
{
    return m_Ipv4_frag;
}
void StackStats::setIpv4Frag(std::shared_ptr<StackProtocolStats> value)
{
    m_Ipv4_frag = value;
    
}
std::shared_ptr<StackProtocolStats> StackStats::getIcmpv4() const
{
    return m_Icmpv4;
}
void StackStats::setIcmpv4(std::shared_ptr<StackProtocolStats> value)
{
    m_Icmpv4 = value;
    
}
std::shared_ptr<StackProtocolStats> StackStats::getIgmp() const
{
    return m_Igmp;
}
void StackStats::setIgmp(std::shared_ptr<StackProtocolStats> value)
{
    m_Igmp = value;
    
}
std::shared_ptr<StackProtocolStats> StackStats::getNd() const
{
    return m_Nd;
}
void StackStats::setNd(std::shared_ptr<StackProtocolStats> value)
{
    m_Nd = value;
    
}
std::shared_ptr<StackProtocolStats> StackStats::getIpv6() const
{
    return m_Ipv6;
}
void StackStats::setIpv6(std::shared_ptr<StackProtocolStats> value)
{
    m_Ipv6 = value;
    
}
std::shared_ptr<StackProtocolStats> StackStats::getIpv6Frag() const
{
    return m_Ipv6_frag;
}
void StackStats::setIpv6Frag(std::shared_ptr<StackProtocolStats> value)
{
    m_Ipv6_frag = value;
    
}
std::shared_ptr<StackProtocolStats> StackStats::getIcmpv6() const
{
    return m_Icmpv6;
}
void StackStats::setIcmpv6(std::shared_ptr<StackProtocolStats> value)
{
    m_Icmpv6 = value;
    
}
std::shared_ptr<StackProtocolStats> StackStats::getMld() const
{
    return m_Mld;
}
void StackStats::setMld(std::shared_ptr<StackProtocolStats> value)
{
    m_Mld = value;
    
}
std::shared_ptr<StackProtocolStats> StackStats::getUdp() const
{
    return m_Udp;
}
void StackStats::setUdp(std::shared_ptr<StackProtocolStats> value)
{
    m_Udp = value;
    
}
std::shared_ptr<StackProtocolStats> StackStats::getTcp() const
{
    return m_Tcp;
}
void StackStats::setTcp(std::shared_ptr<StackProtocolStats> value)
{
    m_Tcp = value;
    
}
std::shared_ptr<StackMemoryStats> StackStats::getHeap() const
{
    return m_Heap;
}
void StackStats::setHeap(std::shared_ptr<StackMemoryStats> value)
{
    m_Heap = value;
    
}
std::vector<std::shared_ptr<StackMemoryStats>>& StackStats::getPools()
{
    return m_Pools;
}
std::shared_ptr<StackElementStats> StackStats::getSems() const
{
    return m_Sems;
}
void StackStats::setSems(std::shared_ptr<StackElementStats> value)
{
    m_Sems = value;
    
}
std::shared_ptr<StackElementStats> StackStats::getMutexes() const
{
    return m_Mutexes;
}
void StackStats::setMutexes(std::shared_ptr<StackElementStats> value)
{
    m_Mutexes = value;
    
}
std::shared_ptr<StackElementStats> StackStats::getMboxes() const
{
    return m_Mboxes;
}
void StackStats::setMboxes(std::shared_ptr<StackElementStats> value)
{
    m_Mboxes = value;
    
}

}
}
}

