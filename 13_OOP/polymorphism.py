"""
	Polymorphism is the ability to leverage the same interface for different
	underlying forms such as data types or classes
	
	class Person has pay_bill() method
	both Student and Millionaire can pay_bill() even if there are some
	changes
"""
#### Little example
class Animal():	
	def talk(self):
		pass
		
class Cat(Animal):
	def talk():
		print("I'm a cat.")

class Eagle(Animal):
	def talk():
		print("I'm an eagle.")
		
c = Cat()
e = Eagle()
c.talk() # "I'm a cat"    they both inherit from Animal, which has talk() method
e.talk() # "I'm an eagle"	but they behave in different way! (since we override methods as we like)
