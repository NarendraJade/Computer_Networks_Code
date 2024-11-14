import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost',8080)
server_socket.bind(server_address)
server_socket.listen(1)
print("Hi Narendra, HTTP server is running on port: ",server_address[1])
while True:
    connection, client_address = server_socket.accept()
    try:
        print("Connection from", client_address)
        request = connection.recv(1024).decode("utf-8")
        print("Request received: ")
        print(request)
        http_response = b"""\
HTTP/1.1 200 OK
Content-Type: text/html
<html>
    <body>
        <h1>Hello Narendra, this is the HTTP over TCP!</h1>
    </body>
</html>
"""
        connection.sendall(http_response)
    finally:
        connection.close() 