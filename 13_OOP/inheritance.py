"""
	Inheritance
	deriving a class from a base class
	and then apply little modifications here and there if needed

	Types of inheritance
	* single: 'a' inherits from 'b'
	* multiple: 'c' inherits from ('a' and 'b')
	* multilevel: 'c' inherits from 'a' which inherits from 'b'

"""
####### SINGLE INHERITANCE
class base1:
	def fun(self):
		print("[class base1 !]")

class sub(base1): 	#we say that a class inherits from another this way
	pass		# we have no methods in the 'sub' class!

obj = sub()
obj.fun() #a sub class can access its parent methods!


####### MULTIPLE INHERITANCE
class First():
	def __init__(self):
		#First has no parent class
		super(First, self).__init__()
		print("first")
		
class Second():
	def __init__(self):
		#Second has no parent class
		super(Second, self).__init__()
		print("second")
		
class Third(First, Second):
	def __init__(self):
		#super().__init__() calls the superior class' __init__() method,
		#passing as args the child class and the self object
		super(Third, self).__init__()
		print("third")

Third()

######## MULTILEVEL INHERITANCE

class Vehicle():
	def __init__(self):
		print("I am a vehicle")
	
	def grandpaInheritance(self):
		print("This is inherited from Vehicle")

class TwoWheels(Vehicle):
	def __init__(self):
		print("I have two wheels")
	
class Bike(TwoWheels):
	def __init__(self):
		print("I am a bike")

class MotorBike(TwoWheels):
	def __init__(self):
		print("I am a motorbike")
		
bike = Bike()
motorbike = MotorBike()

bike.grandpaInheritance()
motorbike.grandpaInheritance()

