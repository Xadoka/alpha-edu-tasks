def open_file_red():
	file = open("hello.txt","r")
	content = file.read()
	print(content)
	file.close()

open_file_red()

def open_file_write():
	file = open("hello.txt","w")
	file.write("Это новый файл.\n")
	file.close()

#open_file_write()