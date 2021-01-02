"""
	scope in python is GLOBAL and LOCAL
"""

#GLOBAL variable are seen from anywhere

a = 'a is global because everyone can access it'

def number():
	b='b is local because only the function can access it.'
	print(a) #ok, because you can access it
	print(b)

#the following will throw an error
#print(b) #cannot access 'b' outside the function (b was declared inside the function)


