import pickle, os

cache_filename = ".syncguy.db"
pickle_protocol = 2

class CachedFileIndex(object):
	__slots__ = ["__root_dir", "__files", "__conn"]
	
	def __init__(self, root_dir):
		self.__root_dir = root_dir
		self.__files = None
		self.load()
		self.update()
		self.save()
		
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
		pass
	
	def save(self):
		cache_file = open(self.cache_path, "wb")
		pickle.dump(self.__files, cache_file, pickle_protocol)
		cache_file.close()
