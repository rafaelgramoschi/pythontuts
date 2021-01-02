"""
	call functions instead of writing same code again and again
	def fun(parameters):
		pass
		
	fun(arguments)
"""

def add(a,b):
	sumnum = a+b
	return sumnum	#return terminates the call to a function and returns
					#something. If return is used in a try-catch, python
					#will first execute the finally clause AND THEN exits the function

a=1
b=2
c=2
d=5
print( add(a,b) )
print( add(c,d) )

#KEYWORDS ARGUMENTS
#you can call a function this way: (no need to remember arguments order)
def funfun(a,b,c,d):
	return a+b+c+d
	
funfun( c=1, b=3, a=1, d=4) #you can't do for example x=5

#DEFAULT ARGUMENTS
def funfun(a,b,c,d=10): #you can assign a default value
	return a+b+c+d

funfun(4,3,2) #19

#IF YOU WANT TO DEFINE A function with variable-arguments length
def info(user, *users):
	print(user)
	print(users)
	
	
info('dede')
info('Tutu', 'deldeldel','gogosh')

#you can pass keyworded arguments:
def myFun(arg1, arg2, *args, **kwargs):
	print("arg1 is: %s" % (arg1) )
	print("arg2 is: %s" % (arg2) )
	if len(args)>1:
		for i in args:
			print("*args are: %s" %(i))
	else:
		print("*args are: %s" %(args) )
	print("**kwargs are: %s" % (kwargs) )
	
myFun(10,20,4,5,6,7,30, identifier=0,keyword='space')
#you can pass arrays/dicts this way (*/**):
myFun('test','play', *[1,2,3], **{'keyword':1,'name':'john'} )
