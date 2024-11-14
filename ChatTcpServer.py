import socket
import threading
def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print(f"[{client_address}]{message}")
            broadcast_message(message,client_socket)
        except:
            break
    client_socket.close()
    print(f"[DISCONNECTED] {client_address} disconnected")
def broadcast_message(message, current_socket):
    for client in clients:
        if client != current_socket:
            try:
                client.send(message.encode("utf-8"))
            except:
                client.close()
                clients.remove(client)
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost',5555))
    server_socket.listen()
    print("[SERVER] Chat server started on port 5555")
    while True:
        client_socket, client_address = server_socket.accept();
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()
clients = []
start_server()



