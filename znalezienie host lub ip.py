import socket

addr = input()

try:
		result = socket.gethostbyaddr(addr)
		print(result[0] + ' ' + ''.join(result[1]) + ''.join(result[2]))
except socket.error:
		print("Erorr")
    
    
##################################################    
    
    
import socket

addr = input()

try:
		result = socket.gethostbyname_ex(addr)
		print(result[0] + ' ' + ''.join(result[1]) + ''.join(result[2]))
except socket.error:
		print("Error")
