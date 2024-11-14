import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost',65432)
server_socket.bind(server_address)
server_socket.listen(1)
print("Echo TCP server is listening on Port: ",server_address[1])
while True:
    connection, client_address = server_socket.accept()
    try:
        print("Connection from", client_address)
        while True:
            data = connection.recv(1024)
            if data:
                print("Received: ", data.decode())
                connection.sendall(data)
            else:
                break
    finally:
        connection.close() 