#servidor
import socket
import threading

host = "127.0.0.1"
port = 6666

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket Creaado")
sock.bind((host, port))
print ("Socket bind completado")
sock.listen(1)
print ("Socket escuchando...")


def worker(*args):
    conn = args[0]
    addr = args[1]
    try:
        print('Conexion con {}.'.format(addr))
        conn.send("Server: Hola cliente".encode('UTF-8'))
        while True:
            datos = conn.recv(4096)
            if datos:
                print('Recibido: {}'.format(datos.decode('utf-8')))

            else:
                print("Desconectado...")
                break
    finally:
        conn.close()

while 1:
    conn, addr = sock.accept()
    threading.Thread(target=worker, args=(conn, addr)).start()