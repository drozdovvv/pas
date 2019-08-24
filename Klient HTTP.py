import socket

data = b''
sum = b''
size = 10000000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.httpbin.org", 80))
s.send("""GET /html HTTP/1.1\r\nHost: www.httpbin.org\r\n\r\n""".encode())
while len(sum) <= size:
		data = s.recv(1000)
		sum+= data
		size = int((sum.split(b'Content length:')[1]).split(b'\r\n'[0][1:]
#print(sum.decode())
s.close
																																																						
sum = sum.decode()
index = sum.find('<html')
content = sum[index:]																																																						
	
text_file = open("index.html","w+")				
text_file.write(content)
																																																						
text_file.close()	
