"""
	OBJECT ORIENTED PROGRAMMING
	with python it's easy
	* reusable code
	* easy to reproduce real world scenarios
	* produce faster, more accurate applications
	
	Python OOP is different from other OOP languages.
	You don't have to write "class" to make a program runnable.
	Python is an interpreted language. Meaning that the code is executed
	line by line, so if an error occurs, it occurs only when that line
	is executed ( not like Java when you compile the code)
"""

"""
	A company wants to create employee information sheet, which will include
	employee ID, name, progress
"""

"""
	A class is a blueprint used to create objects that have same properties
	or attribute as its class
	
	An object is an istance of a class which contains variables and methods
	it is created at RUN-TIME

	modelling something means to describe that something (color, width, height..)
	hence if you have a "model" file, there you have those description
"""

#use class keyword to create a class
class MyClass():
	pass

#instanciate a new object of that class
myObject1 = MyClass()
myObject2 = MyClass()
print(myObject1,"\n",myObject2)

######################### another example ###########################

class MyClass():
	#we define a method
	def hello(self): #the first parameter inside a method must be "self"
		print("hello")
		
obj = MyClass()
obj.hello()

### Class attributes #########
# are attributes shared by all the isntances of that class
# there are two types of attribute:     BUILT-IN and USER DEFINED

class Test():
	"""
		this is a documentation string for .__doc__
	"""
	pass
#BUILT-IN ATTRIBUTES
print( Test.__dict__ )	#dictionary containing the class' namespace*
#*namespace: useful in finding files/code execution, study if you want to do big python code
print( Test.__doc__ )	#class documentation string or None if undefined
print( Test.__name__ )	#class name
print( Test.__module__ )#module name in which the class is defined
print( Test.__bases__ )	#a possibly empty tuple containing the base classes, in the order of their occurrence in the base class list
						#(the class parents, if any)

#DEFINED BY USER
class Test():
	myAttribute = 2
	def printAttribute(self):
		print( self.myAttribute )

x = Test()
x.printAttribute()

#TYPES OF ATTRIBUTES
# public: can be used from outer access
# __private: can be used only inside class
# _protected: can be used only inside class and subclasses

class Test():
	def __init__(self):
		self.__private = 'i am private'		#private attribute __ prefix
		self._protected = 'i am protected'	#protected attibut _  prefix
		self.public = 'i am public'			#public attribute no prefix

me = Test()
#print( me.__private ) #error
print( me._protected )
print( me.public )


### public, __private, _protected METHODS

class Test():
	__privateVar = 2
	def myPublicMethod(self):
		print("I am public")
	def __myPrivate(self):
		print("I am private. I can be accessed only by the class")
	def _protected(self):
		print("I can be accessed by class itself and subclasses")
		
obj = Test()
obj.myPublicMethod()
#this will work because we are in the same class' file
obj._protected()
#error
#obj.__myPrivate()
#we can access private attributes this way:		
obj._Test__myPrivate()
print( obj._Test__privateVar )

#basically public private protected are just convention and not real strict rules
#it is used by programmers to say "hey don't touch this"

#class & instance variable
class Test():
	classVar = (100) 	#class variable is the same for every new instance
						#unless we change it
	def myMethod(self, name):
		self.name = name
		
x = Test()	#we create a new istance of Test class
y = Test()

x.myMethod("Rafael")	#instance variable are those that we assign
y.myMethod("John")		#at the moment of the instantiation of the new object

print("x.classVar: %s" % (x.classVar) )
print("y.classVar: %s" % (y.classVar) )
print("x.name: %s" % (x.name) )
print("y.name: %s" % (y.name) )


#### CONSTRUCTOR AND DESTRUCTOR

class Test: #you can omit () if no argvs are passed
	def __init__(self):
		print("constructor") #used when creating an object
		
	def __del__(self):
		print("destructor")	#used when destructing an object

x = Test()	#the object is created
del x		#the object is deleted


#### MULTIPLE CONSTRUCTORS #############################################

class Date():
	def __init__(self, yy, mm, dd):
		self.year = yy
		self.month = mm
		self.day = dd
		print("Executed from CONSTRUCTOR 1")
		
	#THIS IS A DECORATOR
	@classmethod 	#used to indicate that this is another constructor
					#but it will be used based on the passed arguments
	#cls means "self object", it's like self but for the other constructors
	def dmy(cls, dd, mm, yy):
		cls.day = dd
		cls.year = yy
		cls.month = mm
		print("Executed from CONSTRUCTOR 2")
		#ORDER OF RETURN MUST BE SAME AS __INIT__ parameters
		return cls(cls.year, cls.month, cls.day)

#myDate1 = Date(2019,12,10)
myDate2 = Date.dmy(12,1,2019)
print( myDate2.day )
