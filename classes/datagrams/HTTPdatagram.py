# Headers: 32 bits, 4 bytes
# 
class HTTPdatagram:
    LIST_OF_METHODS = ["GET", "RESPONSE"]
    #parameterized constructor
    def __init__():
        pass
    def __init__(self, method: str, host: str = None, resource: str = None, data: str = None, response_status_code: str = None):
        self.set_method(method)
        self.set_host(host)
        self.set_resource(resource)
        self.response_status_code = response_status_code
        self.data = data
        if method == "POST":
            if data is None:
                raise ValueError ("No data provided for POST method")
            if response_status_code is None:
                raise ValueError ("No response status code provided for POST method")
    def set_method(self, method):
        if method in self.LIST_OF_METHODS:
            self.method = method
        else:
            raise ValueError(f"HTTP method '{method}' not supported")
    def set_host(self, host):
        self.host = host
    def set_resource(self, resource):
        self.resource = resource
    def __str__(self):
        string = ""
        if self.method == "GET":
            string = self.method + " " + self.resource + " HTTP\n"
            string += "Host: " + self.host
        elif self.method == "RESPONSE":
            string = "HTTP " + self.response_status_code + "\n"
            string += "Data: " + str(self.data)
        return string

if __name__ == "__main__":
    h1 = HTTPdatagram("GET", host = "cardhub.com", resource = "favicon.ico")
    print(h1)
    h2 = HTTPdatagram("RESPONSE", data = "Here's the favicon you requested.", response_status_code = "200 OK")
    print(h2)