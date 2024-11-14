import socket 
class Client: 
    def run(self): 
        server_address = ('localhost', 5000) 
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        client_socket.connect(server_address) 
        print(".......Client........") 
        print("Connected") 
        num_frames = int(input("Enter the number of frames to be requested from the server: ")) 
        client_socket.send(bytes([num_frames])) 
        transmission_type = int(input("Enter the type of transmission (Error=1, No Error=0): ")) 
        client_socket.send(bytes([transmission_type])) 
        check = 0  
        if transmission_type == 0: 
            for i in range(num_frames): 
                frame = client_socket.recv(1)[0] 
                print(f"Received frame number: {frame}") 
                print(f"Sending acknowledgement for frame number: {frame}") 
                client_socket.send(bytes([frame])) 
        else: 
            for i in range(num_frames): 
                frame = client_socket.recv(1)[0] 
                if frame == check: 
                    print(f"Received frame number: {frame}") 
                    print(f"Sending acknowledgement for frame number: {frame}") 
                    client_socket.send(bytes([frame])) 
                    check += 1  
                else: 
                    print(f"Discarded frame number: {frame}") 
                    print("Sending NEGATIVE acknowledgement") 
                    client_socket.send(bytes([-1]))
        client_socket.close() 
        print("Quitting") 
if __name__ == "__main__": 
    client = Client() 
    client.run()
