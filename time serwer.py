import socket
import time;

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("localhost", 1769))
s.listen(5)

while True:
    client, addr = s.accept()
    print("Connected: " + addr[0])

    while True:
        data = client.recv(1024)
        if not data:
            break;
        print ('I receive = ' + data.decode('utf-8'))
								time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        client.send(str(time).encode('utf-8'))
    
    client.close()

s.close()


##########################################


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
try: 
    s.connect(('localhost', 1769)) 
    while True: 
        data = input() 
        s.send(data.encode('utf-8')) 
        data = s.recv(1024) 
        if not data: 
            break 
        print ('Response:' + data.decode('utf-8')) 
    s.close() 
except socket.error: 
print ('Error')
