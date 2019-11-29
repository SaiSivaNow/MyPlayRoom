import socket
import threading
  
# next create a socket object 
s = socket.socket()          
  
# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12345                
  
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind(('', port))         
  
# put the socket into listening mode 
s.listen(5)      
  
# a forever loop until we interrupt it or  
# an error occurs 
while True: 
  
   # Establish connection with client. 
   c, addr = s.accept()
   print(c)
   print(addr)
   print(c.recv(1024))
   # send a thank you message to the client.
   header = 'HTTP/1.1 200 OK\n'
   header += 'Content-Type: '+str(mimetype)+'\n\n'
   header+"""<html>
    <body>
    <h1>Hello World</h1> this is my server!
    </body>
    </html>"""
   c.send(header.encode('utf-8'))
   print('Sent finished')
   #c.send('Thank you for connecting'.encode()) 
  
   # Close the connection with the client 
   c.close() 
