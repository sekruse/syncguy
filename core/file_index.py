import pickle, os

cache_filename = ".syncguy.pickle"
pickle_protocol = 2

class Directory(object):
	def __init__(self, name=None):
		self.name = name
		self.files = {}
		self.dirs = {}
		
	def add_file(self, file):
		self.files[file.name] = file
		
	def add_directory(self, dir):
		self.dirs[dir.name] = dir
		
	def get_dir(self, name):
		dir = self.dirs.get(name, None)
		if dir is None:
			dir = Directory(name)
			self.add_directory(dir)
		return dir
		
class File(object):
	def __init__(self, name, mod_time, size, content):
		self.name = name
		self.mod_time = mod_time
		self.size = size
		self.content = content
		
	def __repr__(self):
		return str(self)
		
	def __str__(self):
		return "File('"+self.name+"')"

class CachedFileIndex(object):
	#__slots__ = ["__root_dir", "__files", "__root"]
	
	def __init__(self, root_dir):
		self.__root_dir = os.path.normpath(root_dir)
		self.__files = None
		self.__root = Directory()
		self.load()
		self.update()
		self.save()
		
	@property
	def root(self):
		return self.__root
		
	@property
	def cache_path(self):
		return os.path.join(self.__root_dir, cache_filename)

	def load(self):
		if os.path.exists(self.cache_path):
			cache_file = open(self.cache_path, "rb")
			try:
				self.__files = pickle.load(cache_file)
			except:
				print "Could not load cache file!"
				self.__files = {}
			cache_file.close()
		else:
			self.__files = {}
		
	def update(self):
		for base_dir, dirs, files in os.walk(self.__root_dir, topdown=True):
			base_path = self.split_path(base_dir)
			dir = self.__root
			for path_elem in base_path:
				if len(path_elem) == 0:
					continue
				dir = dir.get_dir(path_elem)
			for file in files:
				file_path = os.sep.join((base_dir, file))
				file_stat = os.stat(file_path)
				mtime = file_stat.st_mtime
				size = file_stat.st_size
				dir.add_file(File(file, mtime, size, 0))
			
	def split_path(self, dir):
		dir = dir[len(self.__root_dir)+1:]
		return dir.split(os.sep)
	
	def save(self):
		cache_file = open(self.cache_path, "wb")
		pickle.dump(self.__files, cache_file, pickle_protocol)
		cache_file.close()
