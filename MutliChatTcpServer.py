import socket 
import threading 
clients = [] 
def broadcast(message, sender_socket): 
    for client in clients: 
        if client != sender_socket: 
            try: 
                client.send(message) 
            except: 
                client.close() 
                clients.remove(client) 
 
def handle_client(client_socket, client_address): 
    print(f"[NEW CONNECTION] {client_address} connected.") 
    while True: 
        try:  
            message = client_socket.recv(1024) 
            if not message: 
                break 
            print(f"[{client_address}] {message.decode('utf-8')}") 
            broadcast(message, client_socket) 
        except: 
            break 
    clients.remove(client_socket) 
    client_socket.close() 
    print(f"[DISCONNECTED] {client_address} disconnected.")  
def start_server(): 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server_socket.bind(('localhost', 5555)) # Bind to a specific IP and port 
    server_socket.listen() 
    print("[SERVER] Chat server started on port 5555...") 
    while True:  
        client_socket, client_address = server_socket.accept() 
        clients.append(client_socket) 
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address)) 
        thread.start()  
start_server()
