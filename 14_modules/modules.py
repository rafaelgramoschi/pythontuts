"""
	Modules
	* logically organize your code (db_connections.py, pdf.py,.. each file has its function)
	* are just python files (.py)
	* files containing Python definition and statements
"""

#use IMPORT to load a module "mymodule.py" in python,
#when the interpreter encounters an import statement, it imports the Module,
#if the Module is present in the search path
# the module gets executed only once!
import math

print( dir(math) )	#return list of strings of names defined by the module
					#(all the variable functions that the module uses)

#FROM allows you to import specific attributes from specific Module into the current namespace
from math import sqrt, tan
#is useful if you want to load minimum things, instead of a full Module

#doing like following, is like import math
#from math import * #but it is used, so you can change the star with the wanted attributes

#reload is used to re-execute a module after it has been loaded
from importlib import reload
reload(math)

"""
	Important modules used in Python:
	* sys - provides access to some variables used or maintained by the interpreter
			and to functions that interact strongly with the interpreter. It's always available
		sys.argv - prints arguments passed to python at command line
		sys.exit() - tells the python interpreter to quit
		sys.winver - version of windows
		sys.flags - status of command line flags
		sys.prefix - returns the path to python virtual environment or installation folder
		
	* os - interact with your os, runs os commands
		os.getcwd() - get current working directory
		os.chdir('../') - change current directory (go back in this case)
		os.mkdir('./rafael') - make new directory
		os.rmdir('./rafael') - remove directory
		os.name - return os name
		os.environ() - return environment variabels (dictionary)
		os.getlogin() - return the username logged in
		os.getppid - parent process id (the process running this python file)
		os.path.join(path, *path) - join intelligently two paths in one
		os.path.abspath(path) - returns absolute path for it (full path to that file/path)
		os.path.normpath(path) - returns normalized path for it (./ won't be part of the path)
		#on windows this converts / to \ inside the path
		os.path.split(path) #returns a splitted path: ('directory', 'filename') tuple
		os.path.exists(path) #return True if path exists
		os.path.isdir(path)	#return True if is a directory
		os.walk(path)	#gives a generator (iterator), so it is used in a for loop
		for i in os.walk(path):
			print(i) #('walked_directory', ['directories'], ['filenames'])
"""
import os
print(os.path.normpath("./") )

#os.walk('./')	#gives a generator (iterator), so it is used in a for loop
for i in os.walk('./'):
	print(i)	#('walked_directory', ['directories'], ['filenames'])

"""
	* math
	* DateTime
	* Random
	* Json
"""
