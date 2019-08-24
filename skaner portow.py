import socket
from socket import AF_INET, SOCK_STREAM

def skaner(port):
		try:
		  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		  result = s.connect_ex(("212.12.14.1",port)) 
		  if result == 0:
				  opened.append(port)
		  else:
				  closed.append(port)
				s.close()
		except socket.error:
				print ("error")
				
strona = input()
porty = input()

for port in porty:
		skaner(strona, port)
