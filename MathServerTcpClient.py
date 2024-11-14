import socket
def send_math_expression(expression):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5555))
    client_socket.send(expression.encode('utf-8'))
    result = client_socket.recv(1024).decode('utf-8')
    print(f"Server Response: {result}")
    client_socket.close()
while True:
    expression = input("Enter a math expression (or 'exit' to quit): ")
    if expression.lower() == 'exit':
        break
    send_math_expression(expression)
