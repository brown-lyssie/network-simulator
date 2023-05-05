from Host import Host
from Graph import Graph
from Packet import Packet

class Network:
    __CHANCE_OF_HOST_FAILURE = .05
    graph = Graph()
    ips_of_down_hosts = []

    #default constructor w optional argument
    def __init__(self, chance_of_host_failure: float = __CHANCE_OF_HOST_FAILURE, log=False, log_file_obj = None):
        self.chance_of_host_failure = chance_of_host_failure
        if log and log_file_obj is None:
            raise FileNotFoundError ("No log file object provided")
    def add_host_to_network(self, ipaddress: str):
        # ensure that host not already in graph
        if self.is_ip_valid(ipaddress):
            self.graph.add_item(Host(ipaddress))
        else:
            raise ValueError ("Invalid IP address supplied")
    def is_host_in_network(self,ip: str):
        return self.graph.is_item_in_graph(Host(ip))
    def is_ip_valid(self, ip: str):
        # NOTE: USING IPV4
        # IPV4 uses 32 bits, 4 sections of 8 bits
        # Example IP address: 
        # 100.100.100.100
        ip_sections = ip.split(".")
        if len(ip_sections) != 4: return False
        for section in ip_sections:
            if len(section) > 3: return False
            try:
                i = int(section, 10)
                if (i > 255):
                    return False
            except ValueError:
                return False
        return True
    def get_incoming_buffer_from_ip(self, ip: str) -> list:
        if self.is_ip_valid(ip):
            if self.is_host_in_network(ip):
                host_index = self.get_host_index_from_ip(ip)
                #return list(self.graph.items[host_index].get_incoming_buffer())
        else:
            raise ValueError ("Invalid IP address supplied")
    def get_host_index_from_ip(self, ip:str) -> int:
        

        return self.graph.get_item_index(Host(ip))
    def insert_incoming_packet(self, ip:str, incoming_item, log = False, log_file_obj = None):
        host_index = self.get_host_index_from_ip(ip)
        successful_insert = self.graph.items[host_index].insert_incoming(incoming_item)
        if log:
            if successful_insert:
                log_file_obj.write(f"Packet with id {incoming_item.get_id()} was inserted into incoming buffer of host with IP address {ip}\n")
            else:
                log_file_obj.write(f"Failed to insert packet with id {incoming_item.get_id()} into incoming buffer of host with IP address {ip}; incoming buffer full\n")
        return successful_insert
    
    #functions you're more likely to use
    def transfer_messages_from_hosts(self, host1_ip, host2_ip, log=False, immediate=True):
        host1_index = self.get_host_index_from_ip(host1_ip)
        print("host1 index", host1_index)
        host2_index = self.get_host_index_from_ip(host2_ip)
        message=self.graph.items[host1_index].pop_incoming()

        print(message)
        

#  test code that is run if you type
# python3 classes/Network.py
if __name__ == "__main__":
    n = Network()
    n.add_host_to_network("127.0.0.26")
    n.add_host_to_network("127.0.0.26")
    n.add_host_to_network("192.10.80.21")
    print(n.is_host_in_network("127.0.0.26"))
    print(n.is_host_in_network("192.10.800.21"))
    print(n.get_incoming_buffer_from_ip("127.0.0.26"))
