"""
	type() is a built in function which returns the type of data type
"""
a = 0.001
print(a)
print( type(a) )
print("\n")
a = 1
print(a)
print( type(a) )
print("\n")
a = "str"
print(a)
print( type(a) )
print("\n")
a = True
print(a)
print( type(a) )
print("\n")
a = [1,2,3]
print(a)
print( type(a) )
print("\n")
a = (1,2,3)
print(a)
print( type(a) )
print("\n")
a = {1,2,3,3,2,1} #{1,2,3} because a set doesn't contain same values
print(a)
print( type(a) )
print("\n")
a = {'Name':'Rafael', 'Desc':'yo'}
print(a)
print( type(a) )


# example of usage
inputA = 1.234 # think of this as user input that must be numeric

if type(inputA) is type(1) or type(inputA) is type(1.1): # if inputA type is int or float
	print(inputA*2)
else: #if it is a string or other, please try again.
	print("An error occured in the input. Dogs were inputted. Pls try again.")
