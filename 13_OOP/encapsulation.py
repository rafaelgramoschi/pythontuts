"""
	Encapsulation
	Combining the code into a public interface,
	and a private implementation of that interface
	
	Mechanism for restricting the access to some components of an object.
	internal representation of an object
	can't be seen from outside the object definition

	encapsulate class, methods and attributes so they can't be accessed easily
	from outside
"""

class CreditCard():
	
	def __init__(self, cn, user, ia):
		self.__cardnumber = cn
		self.user = user
		self.__account = ia
	
	def getAccount(self):
		return("Account: %s" % (self.__account) )
	
	def setCredit(self, credit):
		self.__credit(credit)
	
	def setDebit(self, credit):
		self.__debit(credit)
		
	# private methods, can be accessed by class only
	def __credit(self, credit):
		self.__account += credit
		print("[+++] Credit: %s, Account: %s" % (credit, self.__account) )
	
	def __debit(self, credit):
		self.__account -= credit
		print("[---] Debit: %s, Account: %s" % (credit, self.__account) )

newUsr = CreditCard(1234567890, "Rafael", 100)
#error: can't access private attribute __account
#print( newUsr.__account )
print( newUsr.getAccount() )

#error: can't access private method __credit()
#newUsr.__credit(100)
newUsr.setCredit(100)
newUsr.setDebit(70)
newUsr.setCredit(200)
