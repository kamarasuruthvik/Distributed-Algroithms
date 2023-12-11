import zmq

context = zmq.Context()

class Node:
    def __init__(self, id, port):
        self.id = id
        self.port = port
        self.socket = context.socket(zmq.REP)
        self.socket.bind(f"tcp://*:{port}")

    def send_data(self, target_port, data):
        print(f"{self.id} attempting to send data")
        client = context.socket(zmq.REQ)
        client.connect(f"tcp://localhost:{target_port}")
        client.send_string(data)
        reply = client.recv()
        client.close()
        return reply

    def receive_data(self):
        print(f"{self.id} attempting to receive data")
        message = self.socket.recv_string()
        self.socket.send_string("Ack")
        # Process the message
        print(f"Node {self.id} received: {message}")
