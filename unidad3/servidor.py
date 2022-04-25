import socket

HOST = "127.0.0.1" # Localhost
PORT = 5346

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:    # Parameters specify the address family and the socket type. Using "with" there is no need to call s.close()
    s.bind((HOST, PORT))                                        # Associate the socket to a specific network interface and port number
    s.listen()                                                  # Enable the socket to accept connectios. It makes it a listening socket.
    (csocket, caddress) = s.accept()                            # Blocks and waits for an incoming connection. Get a new socket object.
    with csocket:
        print("Connected by : ", caddress)                      # Prints the name of the client
        while True:
            data = csocket.recv(1024)                           # Read the data from the client
            if not data:                
                break;                                          # When there is no more data, we finish
            
            csocket.sendall(data);  
            print(data)