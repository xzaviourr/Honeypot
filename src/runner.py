import socket
from filesystem import FileSystem 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 23))
s.listen(5)
print("running")
while True:
	c, addr = s.accept()
	print("connected to: ", addr)
	c.recv(4096)
	while True:
		c.send('username: '.encode())
		print(c.recv(4096))
		c.send('password: '.encode())
		print(c.recv(4096))
		c.send('xzaviourr@xzaviourr: '.encode())
		print(c.recv(4096))
	c.close()
