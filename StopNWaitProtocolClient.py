import socket 
import pickle 
class Client: 
    def __init__(self): 
        self.sender = None 
        self.packet = "" 
        self.ack = "" 
        self.msg = "" 
        self.sequence = 0 
        self.i = 0 
    def run(self): 
        try: 
            self.sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            print("Waiting for connection....") 
            self.sender.connect(('localhost', 2005)) 
            self.sequence = 0 
            self.str_msg = pickle.loads(self.sender.recv(1024)) 
            print("receiver >", self.str_msg) 
            packet = input("Enter the data to send: ") 
            n = len(packet) 
            while True: 
                if self.i < n: 
                    self.msg = str(self.sequence) + packet[self.i] 
                elif self.i == n: 
                    self.msg = "end" 
                    self.sender.send(pickle.dumps(self.msg)) 
                    break 
                self.sender.send(pickle.dumps(self.msg)) 
                self.sequence = 1 if self.sequence == 0 else 0 
                print("data sent >", self.msg) 
                self.ack = pickle.loads(self.sender.recv(1024)) 
                print("waiting for ack.....\n\n") 
                if self.ack == str(self.sequence): 
                    self.i += 1 
                    print("receiver > packet received\n\n") 
                else: 
                    print("Timeout resending data....\n\n") 
                    self.sequence = 1 if self.sequence == 0 else 0 
            print("All data sent. Exiting.") 
        except Exception as e: 
            print(f"Client error: {e}") 
        finally: 
            try: 
                self.sender.close() 
            except Exception: 
                pass 
if __name__ == "__main__": 
    client = Client() 
    client.run()
