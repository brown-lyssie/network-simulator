class Packet:
    content = ""
    #default constructor
    def __init__(self):
        pass
    #parameterized constructor
    def __init__(self, s: str):
        self.content = s