import socket               # Import socket module
import time 

username = "Loophac"
type = "Rock"

while True:
    s = socket.socket()         # Create a socket object
    s.connect(('localhost', 12345))
    #s.send("-420,600")
    msg1 = "-420,600"
    s.sendall(msg1.encode())
    s.recv(2048)  # but we don't really care what the message is
    msg2 = username
    s.sendall(msg2.encode()) 
    s.recv(2048)  # but we don't really care what the message is
    msg2 = type
    s.sendall(msg2.encode())   
    time.sleep(6)   

