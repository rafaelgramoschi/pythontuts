"""

	Sets - Mutable Data Type
	* enclosed in CURLY BRACKETS
	* UNORDERED collection of items separated by comma
	* every element is unique (they do not repeat)
	"hello world" = {'l','w','h','o','e','r','d'}  <--remember they are unordered!!
	be aware that H and h are different inside sets!!!

"""

# create a set manually
my_set = {1,2,3,3,3}
print(my_set)#--> {1,2,3} n. 3 appears only once

# you can create sets using built-in function set
myNewSet = set( [1,2,3,4] ) # create a set from a list
print(myNewSet) #--> {1,3,2,4} because sets are unordered you might get this

myNewSet = set( {'Age': 22, 'Country': 'USA'} ) #create set from a dictionary
print(myNewSet) #-->{'Age', 'Country'} the values here are not saved, only keys !!!!

myNewSet = set ( "Hello h world" ) # {'h','e','l','o','w','r','d'}
print(myNewSet)

# SETS OPERATIONS

#UNION
a = {1,2,3}
b = {'a','b','c'}
print(a|b) # {1,2,'a',3,'b','c'}

#INTERSECTION
print(a&b) # empty set because they have nothing in common
a = {1,2,3}
b = {2,3,4}
print(a&b) # {2,3}

#DIFFERENCE
print(a-b) # {1,2,3}-{2,3,4} = {1} # prints a without the elements that are in b

print(1 in a) #True
print( b.issubset(a) ) #True if b is subset of a
print( b.issuperset(a) ) #True if b is superset of a
print( b.union(a) )	# same as b|a={1,2,3,4}
print( b.intersection(a) ) # same as b&a={2,3}
print( b.difference(a) ) #	same as b-a={4}
print( b.symmetric_difference(a) ) # {1,4}

#add, remove, discard, pop, clear
s = {1,2,3,'a'}
print(s)
s.add('b') # adds 'b' to set
print(s)
s.remove(1) # removes number 1 from set if not present, throw error
print(s)
s.discard(3) # removes element from set IF PRESENT
print( s.pop() ) # removes random element and returns its value
print( s )
s.clear() # removes all elements from set
print(s)
