import socket               # Import socket module

s = socket.socket()         # Create a socket object
s.bind(('127.0.0.1', 12345))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   print c.recv(1024)
   c.close()                # Close the connection
