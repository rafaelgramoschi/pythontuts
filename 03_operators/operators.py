"""
	
	Operators
		
	ARITHMETIC,
	+,-,/,*,x**y(x^y), %, //(floor division 10//3=3)
	
	ASSIGNMENT,
	first we do operations, then we assign:
	tot = a+b #you first do (a+b) and then assign to tot
	a = b  a will be the value of b
	a += b same as a = a + b but is faster to write
	a -= b same as a = a - b
	a *= b same as a = a * b
	a /= b same as a = a / b
	a **= b  s.a.  a = a**b
	a //= b  s.a.  a = a//b

	COMPARISON,
	a==b equal to
	a!=b not equal to
	a>b greater than
	a<b less than than
	a>=b greater than or equal to
	a<=b less than or equal to
	
	LOGICAL,
	a and b # returns a if a is False, b otherwise
	True and False #False
	it is useful only with boolean values, since:
	'str1' and 'str2' #will give me always the string after the 'and' operator
	even if I do 'str' and 3, will give me 3
	------------------
	a or b # returns b if b is False, a otherwise
	True or False #True
	it is useful only with boolean values, since:
	'str1' or 'str2' #will give me always the string before the 'or' operator
	even if I do 'str' and 3, will give me 'str'
	
	------------------
	not a # returns True if a is True, False otherwise
	not True #False
	it is useful even with number/string values:
	not 4 #False because 0=False in Python, any other value=True, 4=True, so.. not 4=False
	not 'str' #False, same for strings
	not '' #True
	
	BITWISE,
	binary AND, a&b
	binary  OR, a|b
	binary XOR, a^b
	binary NOT, a~b (press Alt Gr+^, italian keyboard)
	binary Left Shift, a<<b, position of mostleft bit is shifted by b value to the left
	binary Right Shift, a>>b,position of mostright bit is shifted by b value to the right
	
	IDENTITY,
	is, True if the variables on either side point to the same object,
		False otherwise
	2 is 2 #True
	2 is 3 #False
	--------------
	is not, False if variables on either side point to same object,
			True otherwise
	2 is not 3 #True
	2 is not 2 #False
	
	MEMBERSHIP
	in, True if finds a variable in the specified sequence
		False otherwise
	'hi' in ['hi','ciao'] #True
	4 in [1,2,3] #False
	
	not in, True if it does NOT find a variable in the specified sequence
			False otherwise
	'Age' not in {'Name':'Rafael', 'City':'Terni'} #True
	22.5 not in {20,22.5,7} #False, there is 22.5 inside the set!
	
"""
