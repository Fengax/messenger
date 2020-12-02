import socket               # Import socket module
from threading import Thread
import sys
from queue import Queue

def client_messenger(client, addr, name, msg_queue):
    while True:
        try:
            msg = client.recv(1024)
            if msg.decode("utf-8") == '': continue
        except:
            users.remove(name)
            print("[{}]({}) disconnected.".format(addr, name))
            sys.exit()
        msg_queue.put(msg)
        print('[{}]({}) >> {}'.format(addr, name, msg.decode("utf-8")))

def client_receiver(client, addr, msg_queue):
    while True:
        msg = msg_queue.get()
        client.send(msg)

s = socket.socket()
ip = input("IP address of this machine: ")
port = 50000

s.bind((ip , port))
s.listen(5)

users = []
queue = Queue()
while True:
   c, addr = s.accept()
   addr = "{}:{}".format(addr[0], addr[1])
   recv = c.recv(1024)
   type = recv[:8]
   if type == b'messengr':
       name = recv[8:].decode("utf-8")
       if name not in users:
           users.append(name)
           c.sendall(str.encode("good"))
           print("[{}]({}) connected.".format(addr, name))
           thread = Thread(target=client_messenger, args=(c, addr, name, queue,))
           thread.start()
       else:
           c.sendall(str.encode("bad"))
           print("[{}] attempted to use a duplicate name, attempt rejected.".format(addr))
   elif type == b'receiver':
       print("listener connected")
       thread = Thread(target=client_receiver, args=(c, addr, queue,))
       thread.start()
