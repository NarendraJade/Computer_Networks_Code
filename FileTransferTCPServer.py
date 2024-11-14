import socket 
def receive_file(server_socket): 
    print("[SERVER] Waiting for a connection...") 
    client_socket, client_address = server_socket.accept() 
    print(f"[CONNECTED] Connection from {client_address}") 
    filename = client_socket.recv(1024).decode('utf-8') 
    print(f"[RECEIVING FILE] {filename}") 
    with open(filename, 'wb') as file: 
        while True: 
            data = client_socket.recv(1024) 
            if not data: 
                break 
            file.write(data)
    print(f"[FILE RECEIVED] {filename} received successfully!")  
    client_socket.close() 
    print(f"[DISCONNECTED] {client_address} disconnected.") 
def start_server():  
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server_address = ('localhost', 5555) 
    server_socket.bind(server_address)
    server_socket.listen(1) 
    print("[SERVER] File transfer server started on port 5555...") 
    receive_file(server_socket) 
start_server()