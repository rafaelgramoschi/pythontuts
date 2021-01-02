sorted([10,2,45,-1])	#return sorted list from items iterable
all([1,False,'str'])	#return True if all elements passed ARE True (not False, not None, not 0)
any([1,True,'str'])		#return True if at least one element IS True
bool(5)					#from data type to boolean ( bool(1, 'str', True) = True ) ... ( bool(0, None, False) = False )
chr(123) #'{'			#return ASCII code/UNICODE for a given character, it goes up to 255!
abs(-2.567) #2.567		#returns absolute value of a given number
globals()				#
int('500')				#returns int value of given string
len([1,2,3])			#returns length of given object
bin(2)					#converts number into binary string with refix 0b. e.g.: bin(2) = '0b10'
eval('print("eval")')	#executes a string as python code (be aware that some features are disabled by default because of security flaws)
sum([1,2,4])			#sums numeric values in an iterable object (list, tuple, set), do not pass strings inside objects

#reversed(iterable)
for i in reversed([1,2,3]):	#usable only in a loop. it reverses the order of a list
	print(i) #will print 3,2,1

#open(file)
with open('aFile.txt') as f: #it is a best practice to use open with "with"
	pass				#opens a file and returns a file object


#enumerate()				#returns a list of tuples with index values and its items
#e.g:
grocery = ['bread','milk','butter']
enumerateGrocery = enumerate(grocery)

print("Type of enumerate object:")
print( type(enumerateGrocery) )

print("Convert enumerate object to list:")
print( list(enumerateGrocery) ) #[(0, 'bread'), (1, 'milk'), (2, 'butter')]

print("Change default counter (start count from 10 instead of 0)")
enumerateGrocery = enumerate( grocery,10 ) #[(10, 'bread'), (11, 'milk'), (12, 'butter')]
print( list(enumerateGrocery) )

