from datagrams.DNSdatagram import DNSdatagram
class DNSserver:
    def __init__(self) -> None:
        self.NAME_IP_PAIRS = []
    def __init__(self, table: list):
        self.NAME_IP_PAIRS = list
    def get_ip(self, name) -> str:
        for stored_name, ip in self.NAME_IP_PAIRS:
            if name == stored_name:
                return ip
        raise ValueError ("Name requested is not in DNS table")
    def get_datagram(self, name):
        ip = self.get_ip(name)
        return DNSdatagram(name, ip)
    def store_pair(self, name, ip):
        self.NAME_IP_PAIRS.append([name, ip])