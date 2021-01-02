"""
	you can ask user for input with function input()
"""

usr = input("Enter your input: ")
print("Received input is: ", usr)

print("Input type: " + str(type(usr)) )

#type() returns class type of argument

if type(usr) is type(0): #if input data type == <class 'int'>
	print("Input Data type is number")
elif type(usr) is type('0'): #if input data type == <class 'str'>
	print("Input Data Type is string")
else:
	print("Your input is different from string or number")

########
# NOTE: input will be ALWAYS converted to string data type
########

name = input("\nEnter your name: ")

if type(name) is type('abc'):
	print("Name is string")
else:
	print("name is other type")
	
age = input("Enter your age: ")
print("Welcome " + name + ". Your age is " + age)
print("After 5 years your age will be " + str(int(age)+5) )
