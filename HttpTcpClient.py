import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost',8080)
client_socket.connect(server_address)
try:
    request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
    client_socket.sendall(request.encode())
    response = client_socket.recv(1024)
    print("HTTP response from server: ")
    print(response.decode())
finally:
    client_socket.close()
