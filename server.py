import socket               # Import socket module
import sqlite3
import struct
s = socket.socket()         # Create a socket object
s.bind(('127.0.0.1', 12345))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

def db():
   conn = sqlite3.connect('globaldata.db')
   db = conn
   cursor = db.cursor()
   userid = msg1
   geolocation = msg2
   fav = msg3

   cursor.execute('DELETE FROM userData WHERE rowid NOT IN (SELECT min(rowid) FROM userData GROUP BY userid);')
   
 
   cursor.execute('''INSERT INTO userData(userid, geolocation, fav)
                  VALUES(?,?,?)''', (geolocation,userid,fav))
 
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
 
