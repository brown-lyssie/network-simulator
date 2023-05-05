import heapq
from classes.Network import Network
class Simulator:
    def __init__(self, devices_file_name: str, log_file_name: str, chance_of_host_failure = 0, log = False):
        self.queue = []
        self.network = Network(chance_of_host_failure=chance_of_host_failure, log = True, log_file = log_file_name)
        heapq.heapify(self.queue)
        self.generate_devices(devices_file_name)
    def generate_devices(filename):
        with open(filename, "r") as f:
            lines = f.getlines()
            for line in lines:
                if line.startswith("HOST"):
                    pass
                elif line.startswith("SITE HOST"):
                    pass
                elif line.startswith("DNS SERVER"):
                    pass
                elif line.startswith ("ROUTER"):
                    pass
    def generate_links(self, filename):
        with open(filename, "r") as f:
            lines = f.getlines()
            for line in lines:
                split_line = lines.split(" ")
                if line.startswith("LINK"):
                    device1 = self.get_device_with_ip(split_line[1])
                    device2 = self.get_device_with_ip(split_line[2])
                    device1.link_to(split_line[2])
                    device2.link_to(split_line[1])
    def add_event(self, time: int, event: function, printable):
        self.queue.heapadd( (time, event, printable) )
    def handle_event(self, event_tuple):
        pass
    def create_host():
        pass