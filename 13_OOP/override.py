"""
	Method Overriding
	sometimes you need to overwrite a parent's method
"""

class Dad():
	def __init__(self):
		pass

	def presentYourself(self):
		print("I am dad.")

class Son(Dad):
	def __init__(self):
		pass

dad = Dad()				# we create a new istance of class Dad()
dad.presentYourself()	# "I am dad."
son = Son()				# we create a new instance of class Son()
son.presentYourself()	# "I am dad.", this is not what we want it to be

print("---------")
########## so we override the method!
# this means that Dad() has a certain behaviour when presenting himself.
# so we change the behaviour of Son() too, like here.
class Dad():
	def __init__(self):
		pass

	def presentYourself(self):
		print("I am dad.")

class Son(Dad):
	def __init__(self):
		pass
	### HERE WE ADD WHAT SON SHOULD SAY ####
	# we rewrite here how the son should behave when he presents himself
	def presentYourself(self):
		print("I am son.")

dad = Dad()
dad.presentYourself()
son = Son()
son.presentYourself()	# this time, son presents himself as "I am son."


########## ANOTHER EXAMPLE

class Rectangle():
	def __init__(self, length, height):
		self.length = length
		self.height = height

	def getArea(self):
		print(self.length*self.height, " is the area of rectangle.")

class Square(Rectangle):
	def __init__(self, side):
		self.side = side
		Rectangle.__init__(self, side, side)
	
	def getArea(self):
		print(self.side**2, " is the area of the square.")

s = Square(4)
r = Rectangle(4,3)
s.getArea()
r.getArea()
