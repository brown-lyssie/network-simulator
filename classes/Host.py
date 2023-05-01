import queue
class Host:
    ip_address = ""
    __IN_BUFFER_CAPACITY = 10
    __OUT_BUFFER_CAPACITY = 10
    in_buffer_capacity = 0
    out_buffer_capacity = 0
    # private

    ##default constructor
    # USE PARAMETERIZED CONSTRUCTOR PLEASE
    #def __init__(self):
    #    pass
    #parameterized constructor
    def __init__(self, ipaddress: str, in_buffer_capacity:int = __IN_BUFFER_CAPACITY, out_buffer_capacity:int = __OUT_BUFFER_CAPACITY):
        self.ip_address = ipaddress
        self.__incoming_buffer = queue.Queue(maxsize=in_buffer_capacity)
        self.__outgoing_buffer = queue.Queue(maxsize=out_buffer_capacity)
    
    #getters
    def get_incoming_buffer(self):
        return self.__incoming_buffer
    def get_outgoing_buffer(self):
        return self.__outgoing_buffer
    
    #other methods
    def insert_incoming(self, item: any):
        try:
            self.__incoming_buffer.put_nowait(item)
        except queue.Full:
            return -1
        return 0
    def insert_outgoing(self, item: any):
        try:
            self.__outgoing_buffer.put_nowait(item)
        except queue.Full:
            return -1
        return 0

# test code that is ran if we do python3 Host.py
if __name__ == "__main__":
    h = Host(ipaddress="127.0.0.1", in_buffer_capacity=3)
    h.insert_incoming(3)
    h.insert_incoming(4)
    h.insert_incoming(5)
    h.insert_incoming(6)
    print(list(h.get_incoming_buffer().queue))


