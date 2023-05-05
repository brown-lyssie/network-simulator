import queue
class Host:
    ip_address = ""
    __IN_BUFFER_CAPACITY = 10
    __OUT_BUFFER_CAPACITY = 10
    in_buffer_capacity = 0
    out_buffer_capacity = 0
    # private

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
    def peek_incoming(self):
        self.__incoming_buffer.queue.peek()
    def peek_outgoing(self):
        self.__incoming_buffer.queue.peek()

    #setters
    def set_ip_address(self, new_ip: str):
        self.ip_address = new_ip
    
    #overloads
    #NOTE: Use == operator to compare hosts. These will compare only ip_address. Do not use is or is not operators, this compares memory addresses
    def __eq__(self, right_host):
        return self.ip_address == right_host.ip_address
    
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
    def pop_incoming(self):
        return self.__incoming_buffer.queue.pop()
    def pop_outgoing(self):
        return self.__outgoing_buffer.queue.pop()
    def clear_incoming(self):
        self.__incoming_buffer.queue.clear()
    def clear_outgoing(self):
        self.__outgoing_buffer.queue.clear()
#test code that is ran if we type
#python3 Host.py
if __name__ == "__main__":
    h = Host(ipaddress="127.0.0.1", in_buffer_capacity=3)
    h.insert_incoming(3)
    h.insert_incoming(4)
    h.insert_incoming(5)
    h.insert_incoming(6)
    print(list(h.get_incoming_buffer().queue))
    print(h.pop_incoming())
    print(list(h.get_incoming_buffer().queue))
    h.clear_incoming()
    print(list(h.get_incoming_buffer().queue))

    h1 = Host("0.0.0.0", in_buffer_capacity=5, out_buffer_capacity=6)
    h2 = Host("0.0.0.0", in_buffer_capacity=1, out_buffer_capacity=2)
    h3 = Host("1.1.1.1")
    print(h1 == h2)
    print(h2 == h3)
    print(h1 == h3)