"""
	Command Line Parameters
	
	* argument = value passed to a method
	* parameter= variable defined by a method
	
	* it is possible to pass arguments to python programs when executed
	* .argv refers to the number of arguments passed,
	argv[] is a pointer array which points to each argument which is passed to main
	* (sys module) sys.argv: access to any command-line arguments
		- sys.argv is the list of cmd-line arguments
		- len(sys.argv) is the number of cmd-line argv
"""

import sys #import sys module to use sys.argv

# when we launch a python script, we pass arugments like this:
# python3 script.py 'str'
# python3 script.py 1
# python3 script.py 1 2 3 4 5

# argv will be:
# ['script.py', 'str']
# ['script.py', '1']
# ['script.py', '1','2','3','4','5']

# NOTE: the first argv is always the script.py name itself
# numbers, booleans will be passed as string (will become string data type)

# dictionary {'Name':'Rafael', 'Age':22}
# will be passed as ['script.py', 'Name:Rafael', 'Age:22']

print("Check if argv[1] is equal to int 0:")
print("Passed argument: " + sys.argv[1])
print(sys.argv[1] is 0)

print("Check if argv[1] is equal to str '0':")
print("Passed argument: " + sys.argv[1])
print(sys.argv[1] is '0')

print("len(sys.argv): " + str( len(sys.argv) ) )
print(sys.argv)
