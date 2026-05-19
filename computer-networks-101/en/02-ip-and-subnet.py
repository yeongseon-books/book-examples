"""Computer Networks 101 - Episode 2: Ip and subnet."""

# English mirror of the corresponding episode demo
import ipaddress


def summarize_network(cidr: str) -> dict[str, object]:
    """Summarize network."""
    net = ipaddress.ip_network(cidr)
    subnets = list(net.subnets(prefixlen_diff=2))
    return {
        "network": str(net.network_address),
        "broadcast": str(net.broadcast_address),
        "num_addresses": net.num_addresses,
        "first_subnet": str(subnets[0]),
        "contains_192_168_1_42": ipaddress.ip_address("192.168.1.42") in net,
    }


if __name__ == "__main__":
    print(summarize_network("192.168.1.0/24"))
