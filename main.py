import core.files
import sys

if __name__ == "__main__":
	dir = sys.argv[1]
	print "Size of", dir, ":",
	size = core.files.du(dir)
	print size, " bytes"
