"""
	LAMBDA FUNCTIONS ("anonymous" functions)
	
	* defined by the word lambda
	* CAN'T contain commands
	* CAN'T contain more than one expression
	* can take any number of arguments (including optional argv)
		and returns the value of a single expression
		
"""
	# lambda input: action to do to the input and return
ans = ( lambda z: z*4 )	#def or lambda is the same, but this is faster in writing code for short amount of code
# we take a variable name, and we assign a function
print( ans(7) )

ans = lambda z,e: z+e
print( ans(2,5) )

"""
	the biggest use in lambda is passing lambda function as a parameter
	to map()
	
	* map(function, list )
		- map does something for each item inside an iterable object, e.g.: a list
	* filter( function, list )
		- include in the result only the items that solve to True the given function
	* reduce()
		-
"""
#MAP
mylist = [1,2,3,4]
res = map(lambda x: x*2, mylist)
print( list(res) )

#FILTER 
number_list = range(-5,5)
less_than_zero = list( filter( lambda x: x<0, number_list ) )
print(less_than_zero)

#REDUCE return final output out of input
from functools import reduce #to use reduce we need this
product = reduce( lambda x,y: x*y, [1,2,3,4] ) #1*2=2 *3=6 *4=24
print(product)


"""
	A best practice TO CREATE LISTS
	is to use COMPREHENSION LISTS instead of lambda functions
"""
# example from before
mylist = ['a','b','c','d']
res = { c*2 for c in mylist }
print(res)
