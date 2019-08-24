image = 'image.png'

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(config.networkTuple)
    s.listen(5)

    statinfo = os.stat(image)
    size = statinfo.st_size

    while True:

        client, addr = s.accept()
        print("Connected: " + addr[0])
        data = b''
        
        data += client.recv(1024)

        if(data == b"GET_IMAGE \r\n"):

            client.sendall(("SIZE: " + str(size) + " NAME: " + image + "\r\n").encode())
            
            with open(image,'rb') as f:
                print('Starting sending:\n')

                l = f.read(1024)
                           
                while(l):
                    client.send(l)
                    if f:
                        l=f.read(1024)
                
                f.closed
																
					   else:
										client.sendall(("ERROR \r\n").encode())
        
        client.close()
    s.close()

except socket.error:
   print ('Error')
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
data = b''
try:
   s.connect(config.networkTuple)
   s.sendall("GET_IMAGE \r\n".encode())


   data += s.recv(1024)


   id_size = data[0:].find(b'NAME')
   size = (data[6:id_size-1])
   size = int(size.decode())

   name = data[id_size+6:]

   data = b''
   
   while len(data) < size:
      data += s.recv(1024) 

   f = open(name.decode().split('\r\n')[0] + "22", 'wb')
   f.write(data)
   f.close()

   s.close

except socket.error:
   print ('Error')
   
   
   
   
   
   
   
   
   
hostname = 'localhost'
port = 1762
networkTuple = (hostname,port)
