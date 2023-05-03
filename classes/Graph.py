#Graph will be unconnected so that we don't automatically delete our host when we shut it off
#Tbh no need for removing at all for this project
#Note that you need to use self.whatever when calling/using something within a 
class Graph:
    #default constructor
    items = []
    adj_matrix = []

    def __init__(self):
        pass

    def add_item(self, item: any) -> int:
        for i in range(len(self.items)):
            self.adj_matrix[i].append(-1)
        self.adj_matrix.append([-1 for i in range(len(self.items))])
        self.adj_matrix[-1].append(0)
        self.items.append(item)

    def connect_item(self, item1: any, item2: any, weight: int = 1) -> int:
        if not (weight > 0):
            raise ValueError ("Invalid weight: Weight is not greater than 0")
        elif not weight.is_integer():
            raise ValueError ("Invalid weight: Weight is not an integer")
        item1_index = self.get_item_index(item1)
        item2_index = self.get_item_index(item2)
        self.adj_matrix[item1_index][item2_index] = weight
        self.adj_matrix[item2_index][item1_index] = weight
        return 0
    def get_item_index(self, item):
        if self.is_item_in_graph(item):
            return self.items.index(item)
        else:
            raise ValueError (f"{item} not found in graph")
    def is_item_in_graph(self, item):
        return item in self.items


# test code that is run if we type
# python3 Graph.py
if __name__ == "__main__":
    pass
    #from Host import Host
    #h1 = Host("1.1.1.1")
    #h2 = Host("2.2.2.2")
    #g = Graph()
    #g.add_item(h1)
    #g.add_item(h2)
    #print(g.items)
    #print(g.get_item_index(Host("2.2.2.2")))