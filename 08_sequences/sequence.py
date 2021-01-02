"""
	Sequencer
	collections of data type
	
	containers with items that are accessible by indexing or slicing
	len() takes any container as an argument and returns the number of items
	in the container

	a sequence can be a row of motor bikes, or apples
	o o o o

	Sequencer operations
	concatentation (concatenate 2 sequences to create one)
	repetition (take a sequence and multiply by a number)
	membership testing (test if an element is part of a sequence)
	slicing (take a portion of a sequence) [startfrom_included - endhere_excluded]
	indexing (access sequences by index)
	
"""

lst = ['a','b','c']
print(lst[1])		#indexing, b
print(lst[0:2])	#slice, 0 to 2, a,b
print(lst[-1])		#take the last element in the lst, c
print(lst[-2])		#b

print(lst*2)		#repetition, a,b,c,a,b,c
print('a' in lst, 'd' in lst)	#memebership testing, True

"""
	Types of sequences in python
	
	Lists
	
	NEVER USE "list" as the name to a variable to declare a new list.
	list is a built-in function in python.
	doing like this will shadow the function, which won't work anymore.
	
	update, lst[0] = "New value" # this way you update the list
	delete, del(lst[index]) #delete value at a specific index
	lst.pop(index), returns index's value and removes it from list
	lst.remove(value), remove first matching value from list
	lst.append(value), append A item to the end of the list
	lst.extend([val,val..]), append more items to end of list
	lst.insert(index, val), insert item at given position (shifts, does not overwrite!!!)
"""
lst[2] = 0 #update value
print( lst )
del(lst[0]) #delete index 0 (which is 'a')
print(lst)
print(lst[0])

print("\nlist.pop(index)")
lst = ['a','b','c']
lst = lst*2
print( lst.pop(2) ) #returns lst[2], val='c', and removes it from list
print(lst)

print("\nlist.remove(value)")
lst.remove('a')
print(lst)

print( [ x**2 for x in[1,2,3,4,5] ] ) # [1,4,9,16,25]

print("\nlist.append('something')")
lst.append("Hey it's me, Mario")
print(lst)

print("\nlist.extend([1,2])")
lst.extend([1,2])
print(lst)

print("\nlist.insert(0, 'Banana')")
lst.insert(0, 'Banana')
print(lst)

print("\nPrint in reverse order:")
reverse_list = []
#print statement
print( lst[::-1] )
#for loop
for i in lst[::-1]:
	reverse_list.append(i)
print(reverse_list)

lst = ['a','b','x','d','e','z']
print("\nsorted(lst) does not work between int and str.")
print( sorted(lst) )
lst = [1,4,3,2,7,6,5]
print( sorted(lst) )

print("\nTuple inside a List")
lst=[ # this lst will become immutable since contains only tuples!
	(1,2,3),
	("python","pytorch")
]
print(lst)
print( len(lst) )
print( lst[1][0:1] ) #slicing

"""
	Tuples
	faster than list, values can't be changed
	index, repetition, membership testing
	no update
"""

tupn = (1,2,3)
tups = ('a','b','c')

print("\nTuples tupn=(1,2,3) tups=('a','b','c')")
print( "len(tup): " + str( len(tupn) ) + " " + str( len(tups) ) )
print( "max(tup): " + str( max(tupn) ) + " " + max(tups) )
print( "min(tup): " + str( min(tupn) ) + " " + min(tups) )

tup = (0.5, 200,1)
print( sorted(tup) ) # error between str and int
print( tup[::-1] ) # reverse print

print("\nList inside a Tuple")

tup = (
	[1,2,3],
	[4,5,6],
	[7,8,9]
)

print(tup)
print( tup[1][0:2] )
tup[1][0] = 'new' # you CAN modify LISTS, so this will work
print(tup)

print("\nConvert tuple into list. list(tuple)")
lst = list(tup)
print(lst)

print("\nConvert list into tuple. tuple(list)")
tup = tuple(lst)
print(tup)

"""
	Strings
	
	slice works this way, if you have a str="byebye"
	str[startAt:endBefore:skip]
	if i do:
	str[0::2] #output: bb (start at zero, end of string, skip 2 by 2)
	str[::] #start at beginning, end of string, skip nothing
	str[::-1] #start at beginning, end of string, skip -1 (reverse)--> eybeyb
	str[:2] #start at beginning, end before 2, skip nothing-->by
	str[:5:2] #start at beginning, end before 5, skip by 2-->bb
	
	slice, str[0:2]
	update, str[0:2] + 'x'
	concatenate, str1 + str2
	repetition, str*2
	membership, in/not in
	reverse, str[:-1]
"""
str = 'it is ok'
str = """this is
		a string on multiple lines"""
str = "pablo"
print(str)
print(str[2:3])
print(str[0:1]+'x')
print(str+str)
print(str*3)
print("b" in str)
print(str[:-1]) # print from beginning to (:) -1 char --> pabl (o is left out)
print(str[::-1]) # reverse olbap
