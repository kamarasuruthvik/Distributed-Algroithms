import random
import time
from Node import Node


# Example of creating nodes
if __name__ == "__main__":
    node1 = Node(1, 5555)

    print("Activating node!")
    time.sleep(2)
    print("Node are active")
    # Example of node communication
    while True:
        # Node 1 sends data to Node 2
        if random.choice([True, False]):
            print("Sending message!")
            node1.send_data(5556, "Hello from Node 1")
            time.sleep(2)    
