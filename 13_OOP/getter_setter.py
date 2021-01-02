"""
	getter and setter methods
	used to get values or to set values
	you can't set or get values if you don't call those methods.
	It's used to change/get values in a secure way
"""

class Credentials():
	def __init__(self, username):
		self.username = username
	
	def getReverseName(self):
		return( self.username[::-1].upper() )
	
	def setPassword(self, password): # set password by invoking this method
		self.password = password
		
	def getPassword(self):	#get password by invoking this method
		return self.password

newUser = Credentials("Rafael")
newUser.setPassword("password")
print( newUser.password )
print( newUser.getPassword() )
print( newUser.getReverseName() ) #this is another reason you use getters
# otherwise you should have done this:
#print( newUser.username[::-1].upper() ) #every time you would like to print it out
