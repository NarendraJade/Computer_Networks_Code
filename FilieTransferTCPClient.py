import socket 
import os
def send_file(client_socket, filename): 
    client_socket.send(filename.encode('utf-8')) 
    # Open the file and send its contents 
    with open(filename, 'rb') as file: 
        while True: 
            data = file.read(1024) 
            if not data: 
                break 
            client_socket.sendall(data) 
    print(f"[FILE SENT] {filename} sent successfully!") 
def start_client(filename):  
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server_address = ('localhost', 5555) 
    client_socket.connect(server_address) 
    print(f"[CONNECTED] Connected to the server at {server_address}") 
    send_file(client_socket, filename)  
    client_socket.close() 
    print("[DISCONNECTED] Connection closed.") 
filename = 'C:\\Users\\Admin\\OneDrive\\Desktop\\Sample.txt'      
if os.path.exists(filename): 
    start_client(filename) 
else: 
    print(f"[ERROR] File {filename} does not exist.")
