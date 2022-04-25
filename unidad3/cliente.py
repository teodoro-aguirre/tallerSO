import socket

SHOST = '127.0.0.1'      # Localhost
SPORT = 5346

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SHOST, SPORT))
    s.sendall(b"Hello world! This is an echo server made with python.")
    data = s.recv(1024)

print('Received: ' + repr(data))