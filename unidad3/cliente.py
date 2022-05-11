#cliente
import socket

host = "127.0.0.1"
port = 6666

sock = socket.socket()
sock.connect((host, port))

datos = sock.recv(4096)

print(datos.decode('utf-8'))
print("Pata terminar el chat escribe quit")
while True:
  message = input("Escribe un mensaje: ")
  sock.send(message.encode('utf-8'))

  if message == "quit":
    break
    print("bye")
    sock.close()
