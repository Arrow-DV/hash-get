import hashlib
from sys import argv as arg


def hash_file(file):
	hash_type = arg[1].split("-")[1].strip().lower()
	if hash_type not in ['md5','sha256','sha512','sha1']:
		print("-> invaild hash type")
		exit()
	
	try:
		with open(file,'rb') as file:
			_hash_ = hashlib.file_digest(file,hash_type)
			return _hash_.hexdigest() , file.name.split('/')[-1]
	except Exception as error:
		print(f"-> {error}")
		exit()


if len(arg) > 2 :
	file = arg[2]
	print(hash_file(file))
else:
	print("-> Missing Arugs")


