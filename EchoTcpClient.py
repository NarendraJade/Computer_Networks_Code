import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 65432)
client_socket.connect(server_address)
try:
    message = "Hello Echo Server, this a message from Narendra Jade!" 
    print("Server is sending: ",message)
    client_socket.sendall(message.encode())
    data = client_socket.recv(1024)
    print('Received (echo): ', data.decode())
finally:
    client_socket.close()