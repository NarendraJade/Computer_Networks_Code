import socket
import threading
def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected")
    while True:
        try:
            expression = client_socket.recv(1024).decode('utf-8')
            if not expression:
                break
            print(f"[RECEIVED] {client_address}: {expression}")
            try:
                result = eval(expression)
                response = f"RESULT: {result}"
            except Exception as e:
                response = f"Error: {e}"
            client_socket.send(response.encode('utf-8'))
        except:
            break
        client_socket.close()
        print(f"[DISCONNECTED] {client_address} disconnected")
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost',5555))
    server_socket.listen()
    print("[SERVER] Math server started on port 5555")
    while True:
        client_socket, client_address = server_socket.accept()
        thread = threading.Thread(target = handle_client, args=(client_socket, client_address))
        thread.start()
start_server() 