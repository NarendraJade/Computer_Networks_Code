import socket 
import threading 
def receive_messages(client_socket): 
    while True: 
        try: 
            message = client_socket.recv(1024).decode('utf-8') 
            if message: 
                print(message) 
        except: 
            print("An error occurred!") 
            client_socket.close() 
            break 
def send_messages(client_socket): 
        while True: 
            message = input() 
            if message: 
                client_socket.send(message.encode('utf-8')) 
def start_client(): 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client_socket.connect(('localhost', 5555)) 
    print("[CONNECTED] You are now connected to the chat server!") 
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,)) 
    send_thread = threading.Thread(target=send_messages, args=(client_socket,)) 
    receive_thread.start() 
    send_thread.start() 
start_client()

