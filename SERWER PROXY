import socket
import os import config as c

def client_proxy(client):
		proxy =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		proxy.connect(("www.httpbin.org", 80))
		
		print(repr(client))
		data = c.receive_data(client, b'\r\n\r\n')
		proxy.sendall(data)
		
		proxy.close()
		
		
		
		
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost",1770))
s.listen(5)
try:
		while Treu:
				client, addr = s.accept()
				start_new_thread(client_proxy, (client, ))
				
except KeyboardInterrupt:
		s.close()
		
s.close()
