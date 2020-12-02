import socket
from threading import Thread

HOST = input("IP address of server machine: ")  # The server's hostname or IP address
PORT = 50000 # The port used by the server

name = input("Name: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(str.encode("messengr" + name))
    recv = s.recv(1024)
    if recv == b"good":
        while True:
            message = input("Message: ")
            s.sendall(str.encode(name) + b': ' + str.encode(message))
            print("sent")
    else:
        print("Duplicate name, attempt rejected")
