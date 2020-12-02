# messenger

A chatting program built using Python. This program uses a server-client model, utilizing the
local network to communicate with each other.

###Usage 

Run server.py first, on a host machine. IP address would be the IPv4 address of the host machine on that
network. Typically it is 192.168.x.x. Port can be specified to any available port. 
The default is 50000.

Run client.py and view_message.py to send and receive message to/from other people connected
to the server. Enter the host machine's IP address to connect to the server. 

### Limitations

Client cannot send and receive message simultaneously in pure Python. In other words, 
view_message.py and client.py cannot be combined without a 3rd-party GUI library. 
Even with multithreading it will not work. 

Server cannot handle unhandled exceptions that occurs in the client (such as keyboardinterrupt).
If a client exits normally, the disconnect log will appear in the server and the
particular client thread within the server will be closed. In case of an unhandled
exception, the client thread will keep "receiving" empty messages and thus keep running.