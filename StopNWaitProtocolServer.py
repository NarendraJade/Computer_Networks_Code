import socket
import pickle
class Server:
    def __init__(self):
        self.receiver = None
        self.connection = None
        self.packet =  ""
        self.ack = ""
        self.data = ""
        self.i = 0
        self.sequence = 0
    def run(self):
        try:
            self.receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.receiver.bind(('localhost',2005))
            self.receiver.listen(1)
            print("Waiting for connection...")
            self.connection, _ = self.receiver.accept()
            print("Connection established.")
            self.sequence = 0
            self.connection.send(pickle.dumps("Connected"))
            while True:
                self.packet = pickle.loads(self.connection.recv(1024))
                if self.packet == "end":
                    break
                if int(self.packet[0]) == self.sequence:
                    self.data += self.packet[1:]
                    self.sequence = 1 if self.sequence == 0 else 0
                    print("\n\nreceiver > ",self.packet)
                else:
                    print("\n\nreceiver > ",self.packet, "duplicate data")
                if self.i < 3:
                    self.connection.send(pickle.dumps(str(self.sequence)))
                    self.i+=1
                else:
                    self.connection.send(pickle.dumps(str((self.sequence+1)%2)))
                    self.i = 0
                    print("Data received =", self.data)
                    self.connection.send(pickle.dumps("Connection ended"))
        except Exception as e:
            print(f"Server error: {e}")
        finally:
            try:
                self.connection.close()
                self.receiver.close()
            except Exception:
                pass
if __name__ == "__main__":
    server = Server()
    server.run()