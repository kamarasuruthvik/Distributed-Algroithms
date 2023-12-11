import hashlib

class DHT:
    def __init__(self):
        self.table = dict()
    
    def add_node(self, node_data, nodes=1):
        x = self._hash(str(node_data))
        self.table[x]=(x % nodes)

    def _hash(self, key):
        return int(hashlib.md5(key.encode()).hexdigest(), 16)
    
    def get_node(self, node_data):
        x = self._hash(str(node_data))
        if( x in self.table):
            print(f"The data belongs to node {self.table[x]}")
        else:
            print("The data is not present")

    def print_table(self):
        for key, node in self.table.items():
            print(f"Hash: {key}, Node: {node}")


if __name__ == "__main__":
    total_nodes = 5
    total_data = 8
    dht = DHT()
    
    for i in range(0, total_data):
        dht.add_node(i, total_nodes)
            
    dht.print_table()
    dht.get_node(3)
    dht.get_node(10)