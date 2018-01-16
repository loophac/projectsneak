import socket               # Import socket module
import sqlite3
import struct
s = socket.socket()         # Create a socket object
s.bind(('127.0.0.1', 12345))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

def db():
   conn = sqlite3.connect('db/globaldata.db')
   db = conn
   cursor = db.cursor()
   coordinate = msg1
   username = msg2
   taste = msg3
 
   cursor.execute('''INSERT INTO coordinates(Coordinates, Username, Taste)
                  VALUES(?,?,?)''', (coordinate,username,taste))
 
   print('Data Entered')
 
   db.commit()
   db.close()
   return 


while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   msg1 = c.recv(128).decode()
   c.send(b'Got it')
   msg2 = c.recv(128).decode()
   c.send(b'Got it')
   msg3 = c.recv(128).decode()
   #data = c.recv(1024)
   #print data
   #stringdata = data.decode('utf-8')
   c.close()                # Close the connection
   db()
 


