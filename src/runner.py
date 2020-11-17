import socket
from filesystem import FileSystem 
from logger import get_logger
import os
from _thread import *
import threading
from datetime import datetime


class Server:
	def __init__(self):
		self.log = get_logger('honey_pot')
		self.log.info("Server Initiated")
		self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.soc.bind(('', 23))
		self.soc.listen(5)
		self.log.info('Server Active')
		self.thread_lock = threading.Lock()
		self.file_system = FileSystem()

	def __accept_requests(self):
		def __threaded(c, client_ip):
			start = datetime.now()
			c.recv(4096)
			c.send('username: '.encode())
			self.log.warning('username: ' + str(c.recv(4096)))
			c.send('password: '.encode())
			self.log.warning('password: ' + str(c.recv(4096)))
			while True:
				path = self.file_system.pathname
				c.send(('xzaviourr@xzaviourr:' + str(path)).encode())
				data = str(c.recv(4096))
				data = data[2: -5]
				if data == 'quit':
					break
				reply = self.__process_input(data)
				c.send(reply.encode())

				if (datetime.now() - start).total_seconds() > 300:
					c.send('Client disconnected'.encode())
					break

			self.thread_lock.release()
			c.close()

		while True:
			c, addr = self.soc.accept()
			self.log.warning('connected to: ' + str(addr))
			self.thread_lock.acquire()
			start_new_thread(__threaded, (c, addr[0],))

	def __process_input(self, data):
		functions = self.file_system.functions
		frag = data.split(" ")
		frag = list(filter(lambda x: (x != ''), frag))
		self.log.info(str(frag))
		fun = functions[frag[0]]
		for i in range(1, len(frag)):
			fun  = fun[:-1] + r'"{}",)'.format(frag[i])
		if len(frag) > 1:
			fun = fun[:-2] + ')'

		self.log.info(fun)
		exec('self.file_system.' + fun)
		reply = self.file_system.reply + '\n'
		self.log.info(str(reply))
		return str(reply)

	def controller(self):
		self.__accept_requests()

obj = Server()
obj.controller()

