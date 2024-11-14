import socket 
addr = ('localhost', 8011) 
connection = socket.create_connection(addr) 
out = connection.makefile('wb') 
in_stream = connection.makefile('rb') 
try: 
    v = [0] * 8 
    p = in_stream.read(1)[0] 
    print(f"No of frames: {p}") 
    for i in range(p): 
        v[i] = in_stream.read(1)[0] 
        print(v[i]) 
    v[5] = -1 
    for i in range(p): 
        print(f"Received frame is: {v[i]}") 
    for i in range(p): 
        if v[i] == -1: 
            print(f"Request to retransmit from {i + 1} again") 
            n = i 
            out.write(bytes([n])) 
            out.flush() 
    v[n] = in_stream.read(1)[0] 
    print(f"Received frame is: {v[n]}") 
    print("Quitting") 
finally: 
    in_stream.close() 
    out.close() 
    connection.close()
