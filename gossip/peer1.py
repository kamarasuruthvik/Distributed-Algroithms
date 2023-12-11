import zmq
import time
from Node import Node

context = zmq.Context()

# Example of creating nodes
if __name__ == "__main__":
    node2 = Node(2, 5556)

    print("Activating node!")
    time.sleep(2)
    print("Node is active")
    # Example of node communication
    while True:
        node2.receive_data()

