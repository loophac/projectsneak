import socket               # Import socket module
import time 
while True:
    s = socket.socket()         # Create a socket object
    s.connect(('localhost', 12345))
    s.sendall("-420,600")
    s.close()    
    time.sleep(6)   

