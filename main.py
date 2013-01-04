import core.files, core.file_index
import sys

if __name__ == "__main__":
	file_index = core.file_index.CachedFileIndex(sys.argv[1])
