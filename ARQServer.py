import socket 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.bind(('localhost', 8011)) 
server_socket.listen(1) 
a = [30, 40, 50, 60, 70, 80, 90, 100] 
print("Waiting for connection") 
client_socket, _ = server_socket.accept() 
dis = client_socket.makefile('rb') 
dos = client_socket.makefile('wb') 
try: 
    y = len(a) 
    dos.write(bytes([y])) 
    dos.flush() 
    for i in range(y): 
        dos.write(bytes([a[i]])) 
        dos.flush() 
    k = dis.read(1)[0] 
    dos.write(bytes([a[k]])) 
    dos.flush() 
finally: 
    dis.close() 
    dos.close() 
    client_socket.close() 
    server_socket.close()
