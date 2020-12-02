import socket
import time

HOST = 'localhost'  # The server's hostname or IP address
PORT = 50000 # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(str.encode("receiver"))
    while True:
        data = s.recv(1024)
        print(data.decode("utf-8"))