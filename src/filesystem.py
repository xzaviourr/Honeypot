from pyfakefs import fake_filesystem


class FileSystem:
	def __init__(self):
		self.filesystem = fake_filesystem.FakeFilesystem()
		self.os_module = fake_filesystem.FakeOsModule(self.filesystem)
		self.pathname = '/test_dir/'

	def create_file(self, file_name, contents):
		new_file = self.filesystem.create_file(self.pathname + str(file_name), contents=contents)

	def read_file(self, file_name):
		file_module = fake_filesystem.FakeFileOpen(self.filesystem)
		data = ""
		for line in file_module(self.pathname + str(file_name)):
			data += line
		return data

	def ls(self):
		return self.os_module.listdir(self.os_module.path.dirname(self.pathname))

# obj = FileSystem()
# obj.create_file('test1.txt', 'Hello World \nI am a programmer')
# print(obj.read_file('test1.txt'))
# print(obj.ls())
