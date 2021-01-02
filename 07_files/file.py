"""
	How to Handle Files in Python
	REALLY IMPORTANT (ALWAYS DO)
	1) Open file (can't work with a file if not opened)
		open files in current useful mode (r,w...)
	2) Close file:
		opened files are stored into RAM,
		if you don't close that, you can cause a memory leak
		memory leak is when you don't manage memory release as you should
	other:
	1) read file
	2) write file
	3) renaming, move, delete file
"""

# my_file = open('str_path_name', 'str_access_mode')
# access modes:

# WRITE/READ NO OVERWRITE/CREATE NEW
# r		read only
# r+	read and write (NOT overwrite/create new)
# rb	reads binary format only
# rb+	reads and write binary format only (NOT overwrite/create new)

# OVERWRITE/CREATE NEW
# w		write only, overwrite file if exists, create new one if not exists
# w+	read and write (overwrite/create new)
# wb	write only binary format (overwrite/create new)
# wb+	read write binary format (overwrite/create new)

# APPEND TO A FILE (UPDATE, LOGs...)
# a		append only (NOT overwrite/create new)
# a+	append and read
# ab	append binary format
# ab+	append and read binary format

# write to OPENED file:
# my_file = open('/path/to/file.txt', 'r+')
# my_file.write('str\n')
# we include \n to end line
# if you want to write binary code, open a file in binary mode

# read from OPENED file:
# my_file = open('file.txt', 'r')
# my_file.read() # read all file
# my_file.read([count]) # read given number of chars

# RENAME FILE
# for this you need to import os module (import os)
# os.rename('current_name', 'new_name')

# DELETE FILE
# os.remove('file_name')

# CLOSE FILE
# file.close()
# Python automatically close a file,
# when the reference object of a file
# is reassigned to another file 
# f = open('A.txt', 'r')
# if i then do:   f = 2    OR
# f = open('B.txt', 'r') # python closes A.txt, opens B.txt

# File Object Methods
# f.close()
# f.seek( offset[, from] )
# goto: in bytes,
# from: 0=beginning, 1=current file position, 2=end of file
# f.seek(-3, 2) #go to 3rd byte from end of file
# f.tell() return current position in the file (where the next read/write operation will start from in bytes)
# Attributes
# f.mode returns current access mode
# f.name returns the name
# f.softspace no more supported in pyton3

import os

f = open('file.txt', 'w+')
print( f.name + " opened in mode: " + f.mode )
for i in range(0,10):
	f.write(str(i+1) + ") Iteration for loop!\n")
print( f.tell() )
f.close()

f = open('file.txt', 'r')
f.seek(10)
print( f.read(5) ) # read first 5 chars
f.close()

# BEST PRACTICE USE WITH!!!
""" The advantage is that the file is properly closed
after its suite finishes, even if an exception is raised at some point.
Using with is also much shorter than writing equivalent try-finally blocks"""
with open('file.txt', 'rb') as f:
	f.seek(-3,2) # seek can be used only on binary files
	print( f.read(1) )
print(f.closed)
os.rename('file.txt', 'renamed.txt')
os.remove('renamed.txt')

