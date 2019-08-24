def response():
		response = s.recv(2048)
		print(str(response))
		print('\n')
		
		
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('poczta.interia.pl',587))
response()

msg = 'EHLO Matt\r\n'
s.send(msg.encode('utf-8'))
response()

msg2 = 'AUTH LOGIN\r\n'
s.send(msg2.encode('utf-8'))
response()

msg3 = 'YW5uLnJlZC5mb3g3NUBnbWFpbC5jb20K\r\n'
s.send(msg3.encode('utf-8'))
response()

msg4 = 'NzVhZm9oaXYKCg==\r\n'
s.send(msg4.encode('utf-8'))
response()

adres_nadawcy = input('wpisz adres nadawcy')	
msg5 = 'MAIL FROM: <' + str(adres_nadawcy) + '>\r\n'
s.send(msg5.encode('utf-8'))
response()

adres_odbiorcy = input('wpisz adres odbiorcy')	
msg6 = 'RCPT TO: <' + str(adres_odbiorcy) + '>\r\n'
s.send(msg6.encode('utf-8'))
response()

msg7 = 'DATA\r\n'
s.send(msg7.encode('utf-8'))
response()

msg = 'To: <' + str(adres_odbiorcy) +  '\r\n'
s.send(msg.encode('utf-8'))
response()

msg = 'From: <' + str(adres_nadawcy) +  '\r\n'
s.send(msg.encode('utf-8'))
response()

Subject = input('wpisz Subject')
msg = 'Subject: ' + str(Subject) + '\r\n'
s.send(msg.encode('utf-8'))
response()

msg = 'MIME-Version: 1.0\r\n'
s.send(msg.encode('utf-8'))
response()

msg = 'Content-Type: multipart/mixed; boundary="sep"\r\n'
s.send(msg.encode('utf-8'))
response()

msg = '--sep\r\n'
s.send(msg.encode('utf-8'))
response()

message = input('wpisz message')
msg = str(message) + '\r\n'
s.send(msg.encode('utf-8'))
response()

msg = '--sep\r\n'
s.send(msg.encode('utf-8'))
response()

msg = 'Content-Type: text/plain; charset-us-ascii; name="plik.txt"\r\nContent-Disposition: attachment; filename="plik.txt"\r\n'
s.send(msg.encode('utf-8'))
response()

plik = open('plik.txt')
try:
		tekst = plik.read()
finally:
		plik.close()
msg = str(plik) + '\r\n'
s.send(msg.encode('utf-8'))
response()

msg = '--sep\r\n'
s.send(msg.encode('utf-8'))
response()

s.send(end.encode())
s.send("\r\n.\r\n.encode())
response()
							
msg = 'QUIT\r\n'
s.send(msg.encode('utf-8'))
response()
s.close()
