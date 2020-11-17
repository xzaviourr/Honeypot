from pyfakefs import fake_filesystem
from os.path import exists as my_exists
import random


class FileSystem:
	def __init__(self):
		self.filesystem = fake_filesystem.FakeFilesystem()
		self.os_module = fake_filesystem.FakeOsModule(self.filesystem)
		self.pathname = '/'
		self.allow_root_user = False
		self.create_file_system()
		self.functions = {
		"touch": "create_file()",
		"cat": "read_file()",
		"ls": "ls()",
		"dir": "dir()",
		"cd": "cd()",
		"pwd": "pwd()",
		"mkdir": "mkdir()",
		"set_uid": "set_uid()",
		"reset_ids": "reset_ids()",
		"is_root": "is_root()",
		"path": "path()",
		"get_path": "get_path()",
		"rm": "rm()",
		"rmdir": "rmdir()"
		}
		reply = ""

	def create_file(self, file_name, contents):
		if self.check_if_exists(self.pathname + str(file_name)):
			self.reply = ""
			return
		new_file = self.filesystem.create_file(self.pathname + str(file_name), contents=contents)
		self.reply = ""

	def read_file(self, file_name):
		file_module = fake_filesystem.FakeFileOpen(self.filesystem)
		data = ""
		for line in file_module(self.pathname + str(file_name)):
			data += line
		self.reply = data
		return data

	def check_if_exists(self, filepath):
		return self.os_module.path.exists(filepath)

	def ls(self):
		self.reply = ""
		for x in list(self.os_module.listdir(self.os_module.path.dirname(self.pathname))):
			self.reply += str(x) + '\t'
		return self.reply

	def dir(self):
		self.reply = ""
		for x in list(self.os_module.listdir(self.os_module.path.dirname(self.pathname))):
			self.reply += str(x) + '\t'
		return self.reply

	def cd(self, directory):
		self.pathname += str(directory) + "/"
		self.reply = ""

	def pwd(self):
		self.reply = self.pathname
		return self.reply

	def mkdir(self,directory_name):
		new_directory = self.filesystem.create_dir(self.pathname+str(directory_name))
		self.reply = ""

	def set_uid(uid):
		global USER_ID
		USER_ID = uid
		self.reply = ""

	def reset_ids(self):
		set_uid(1 if IS_WIN else self.os_module.getuid())
		self.reply = ""

	def is_root():
		self.reply = str(USER_ID==0)
		return self.reply

	def path(self):
		"""Return the full path of the current object."""
		names = []
		obj = self
		while obj:
		    names.insert(0, obj.name)
		    obj = obj.parent_dir
		sep = self.filesystem._path_separator(self.name)
		if names[0] == sep:
		    names.pop(0)
		    dir_path = sep.join(names)
		    # Windows paths with drive have a root separator entry
		    # which should be removed
		    is_drive = names and len(names[0]) == 2 and names[0][1] == ':'
		    if not is_drive:
		    	dir_path = sep + dir_path
		else:
		    dir_path = sep.join(names)
		dir_path = self.filesystem.absnormpath(dir_path)
		self.reply = dir_path
		return self.reply

	def GetPath(self,):
		self.reply = self.pathname
		return self.pathname

	#Remove file
	def rm(self,directory_name):
		self.os_module.remove(self.pathname+str(directory_name))
		self.reply = ""

	def rmdir(self,directory_name):
		try:
			self.os_module.rmdir(self.pathname+str(directory_name))
			self.reply = ''
		except OSError as error:
			self.reply = 'file cannot be deleted'

	def cat(self, file_name):
		file_module = fake_filesystem.FakeFileOpen(self.filesystem)
		data = ""
		for line in file_module(self.pathname + str(file_name)):
			data += line
		self.replyl = data
		return data

	def cat2(self, file_name, file_name2):
		file_module = fake_filesystem.FakeFileOpen(self.filesystem)
		data=""
		for line in file_module(self.pathname+str(file_name)):
		    data+=line
		data+='\n'
		for line in file_module(self.pathname+str(file_name2)):
		    data+=line
		return data

	def get_random_string(self, length):
	        # put your letters in the following string
	        sample_letters = 'abcdefghijklm'
	        result_str = ''.join((random.choice(sample_letters) for i in range(length)))
	        # print("Random string is:", result_str)
	        return result_str

	def create_file_system(self):
		list = ['bin','boot','cdrom','dev','etc','home','lib','lib32','lib64','libx32','media','mnt','opt',
		'proc','root','run','sbin','snap','srv','sys','tmp','usr','var']

		n = len(list)
		for i in range(n):
		    s = '/' + list[i]+'/'+list[i]+'.txt'
		    self.create_file(s,'This is '+list[i]+' directory')
		    r = random.randint(0,10)
		    for j in range(r):
		        direct ='/' + list[i]+'/'+ str(self.get_random_string(3))
		        self.create_file(direct, 'This is '+direct+' directory')
