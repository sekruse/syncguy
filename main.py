import core.files, core.file_index
import sys

def walk(dir, indent=""):
	print indent, "D", dir.name
	print indent, "=" * (len(str(dir.name))+2)
	for file in dir.files.values():
		print indent, "F", file
	for subdir in dir.dirs.itervalues():
		walk(subdir, indent + "-")

if __name__ == "__main__":
	file_index = core.file_index.CachedFileIndex(sys.argv[1])
	walk(file_index.root)
