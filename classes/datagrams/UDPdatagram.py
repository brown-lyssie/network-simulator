class UDPdatagram:
    def __init__(self, source_port: str, dest_port: str, length: int, data):
        self.set_source_port(source_port)
        self.set_destination_port(dest_port)
        self.set_length(length)
        self.data=data
        self.set_checksum()
    def set_source_port(self, source_port):
        self.source_port = source_port
    def set_destination_port(self, destination_port):
        self.destination_port = destination_port
    def set_length(self, length):
        self.length = length
    def set_checksum(self):
        # for our purposes, checksum will not be used, so will = 0
        self.checksum = 0
    def __str__(self):
        return f"""Source port: {self.source_port}
Destination port: {self.destination_port}
Length: {self.length}
Checksum: {self.checksum}
Data: [{str(self.data)}]"""
    
if __name__ == "__main__":
    u1 = UDPdatagram(53, 53, 250, "IP address = 200.200.150.101")
    print(u1)