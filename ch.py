import hashlib
import bisect

class ConsistentHashing:
    def __init__(self, nodes, replicas=3, ring_size = 32):
        self.replicas = replicas
        self.nodes = nodes
        self.ring_size = ring_size
        self.ring = dict()
        self.node_array = []
        
        for i in range(1, nodes+1):
            self.add_node(i)
           
    def add_node(self, node):
        for i in range(0, self.replicas):
            key = self._hash(f"{node}: {i}")
            hash_val = key % self.ring_size
            self.ring[hash_val] = node
            self.node_array.append(hash_val)
        
        self.node_array.sort()
        
    def _hash(self, key):
        return int(hashlib.md5(key.encode()).hexdigest(), 16)
    
    def print_ring(self):
        for key, node in self.ring.items():
            print(f"Hash: {key}, Node: {node}")
            
    def get_data(self, data):
        hash = self._hash(data)% self.ring_size
        index = bisect.bisect_right(self.node_array, hash)
        key = self.node_array[index]
        print(f"key: {data}, the hash: {hash} the node: {self.ring[key]}")
        
    
if __name__ == "__main__":
    total_nodes = 5
    replicas = 3
    ring_size = 1024
    data = ["d1", "d2", "d3"]
    ring = ConsistentHashing(total_nodes, replicas, ring_size)
    ring.print_ring()
    
    for d in data:
        ring.get_data(d)