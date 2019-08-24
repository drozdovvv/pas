# coding=utf-8
import socket
import threading

class runner(threading.Thread):
		def __init__(self, liczba, client):
				self.numer = liczba
				self.client = client
				threading.Thread.__init__(self)
				
		def run(self):
						numbers =[0,1]
						new = 0
						if liczba == 0:
								client.send("0".encode())
						elif liczba == 1:
								client.send("1".encode())
						else:
								for i in range liczba:                  
										new = numbers[-1] + numbers[-2]   
										numbers.append(new)               
										print 'nowa liczba ciagu: %new' % self.numer
										client.send(str(numbers[-1]).encode())
						client.close()

		 
						
						
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
        print ('ciag Fibonacciego z liczby: ' + data.decode('utf-8'))
								watek = runner(data.decode('utf-8'),client)
								watek.start()
								watek.join()

s.close()





#############################





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
        print ('ostatnia liczba ciagu Fibonaccego:' + data.decode('utf-8')) 
    s.close() 
except socket.error: 
print ('Error')
