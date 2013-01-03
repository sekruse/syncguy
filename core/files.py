import os

def du(root_dir):
	sum = 0
	count = 0
	for root, dirs, files in os.walk(root_dir):
		for file in files:
			file_path = os.path.join(root_dir, root, file)
			#stat = os.stat(os.path.join(root_dir, root, dir))
			if count % 1000 == 0:
				print count, "\t", file_path
			count+=1
			#sum += stat.st_size
	return sum
