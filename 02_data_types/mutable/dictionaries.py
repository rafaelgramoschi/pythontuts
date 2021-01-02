"""
	Dictionaries - Mutable Data Type
	* enclosed in CURLY BRACKETS
	* UNORDERED collection
	* contain key:value pairs separated by comma (,)
	* key must be string or int, values can be anything
"""

dicto = {'Name' : 'Rafael', 'Age': 22}
print(dicto) #--> {'Name' : 'Rafael', 'Age': 22}

# access values by key instead of index!
print(dicto['Name']) #--> Rafael

# dicts can contain anything, key must be string or int
# dicto = { 'Key' : value }
# OR dicto= { int : value }

dicto = {
		'Name' : 'Rafael',
		'Age': 22,
		'Jobs' : [0, 'python'],
		'City': {
					'Name': 'Terni',
					'Country': 'Italy'
					}
		
		}
print(dicto)

#UPDATE
dicto['Jobs'][0] = 1
print(dicto)

#DELETE
del(dicto['City'])
print(dicto)

#len, str, type
print( len(dicto) )	# length of dictionary
print( type(dicto) ) #<class 'dict'>
print( type( str(dicto) ) )	#turn dicto into a string, the type will be <class 'str'> now

#GET
# if you try dicto['Key'] it will throw an error
dicto.get('Key') # will return None instead of an error

#ITEMS
print( dicto.items() ) #return items in form of tuples = [('Name','Rafael'),('Age',22),('Jobs',[1,'python'])]
#KEYS
print( dicto.keys() )	#return keys in dictionary as tuple = (['Name','Age','Jobs'])
#VALUES
print( dicto.values() )	#return values in dictionary as tuple

#DEFAULT
print( dicto.setdefault(1,4) )	#adds (key,value) if not existing in dictionary
# if i try dicto.setdefault('Name', value), since the key is already existing,
# it will return the value for that key ('Rafael')

#COPY
print( dicto.copy() ) #copy dictionary
#DELETE
print( dicto.clear() ) #delete full dictionary

#dictionaries are unordered. to iterate in ordered way:
for item in sorted( dicto.keys() ): #sort dicto based on key names
	pass

