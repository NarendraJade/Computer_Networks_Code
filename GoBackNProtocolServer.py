import socket 
import time 
class Server: 
    def __init__(self): 
        self.frames_sent = 0 
    def run(self): 
        print("...........Server............") 
        print("Waiting for connection....") 
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        server_socket.bind(('localhost', 5000)) 
        server_socket.listen(1) 
        client_socket, _ = server_socket.accept() 
        print("Received request for sending frames") 
        frames_to_send = client_socket.recv(1)[0] 
        received_frames = [False] * frames_to_send 
        transmission_type = client_socket.recv(1)[0] 
        print("Sending....") 
        if transmission_type == 0:
            for i in range(frames_to_send): 
                print(f"sending frame number {i}") 
                client_socket.send(bytes([i])) 
                print("Waiting for acknowledgement") 
                time.sleep(3) 
                ack = client_socket.recv(1)[0] 
                print(f"Received acknowledgement for frame {i} as {ack}") 
        else:  
            for i in range(frames_to_send): 
                if i == 2: 
                    print(f"Skipping sending frame number {i}") 
                else: 
                    print(f"Sending frame number {i}") 
                    client_socket.send(bytes([i])) 
                    print("Waiting for acknowledgement") 
                    time.sleep(3) 
                    ack = client_socket.recv(1)[0] 
                    if ack != -1: 
                        print(f"Received acknowledgement for frame {i} as {ack}") 
                        received_frames[i] = True 
            for i in range(frames_to_send): 
                if not received_frames[i]: 
                    print(f"Resending frame {i}") 
                    client_socket.send(bytes([i])) 
                    print("Waiting for acknowledgement") 
                    time.sleep(2) 
                    ack = client_socket.recv(1)[0] 
                    print(f"Received acknowledgement for frame {i} as {ack}") 
                    received_frames[i] = True 
        client_socket.close() 
        server_socket.close() 
if __name__ == "__main__": 
    server = Server() 
    server.run()
