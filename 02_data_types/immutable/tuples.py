"""

	Tuples - Immutable Data Type
	* enclosed in ROUND BRACKETS
	* values separated by comma
	* can contain objects of different data type

"""
#    index:   0 1 2 3
my_tuple_a = (1,2,3.4)
#    index:      0        1
my_tuple_b = ("string", 5.1425)

print(my_tuple_a) # --> (1,2,3.4)
print(my_tuple_b) # --> ("string", 5.1425)

# access by index
print(my_tuple_b[0]) #--> "string"

# tuples can't be mutable, so the following code will give error
#my_tuple_a[2] = 5.5 # error (tuple doesn't support item assignment)
# for this purpose there are LISTS

# tuples can contain lists too, but they can't be changed from the tuple!
my_tup = ( [1,1,1], "string", (2,2,2) )
print(my_tup)
#my_tup[0] = ["changed","list"] #won't work (can't modify tuple)
print(my_tup[0])
