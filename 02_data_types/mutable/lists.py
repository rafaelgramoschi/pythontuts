"""

	Lists - Mutable Data Type
	* enclosed in SQUARE BRACKETS
	* ordered set of elements
	* lists are slower than tuples, but can be modified
	
"""
my_list = [] # you can create an empty list
my_list = [1,2,3.573,"string"] # and then populate it

print(my_list[3])

my_list[3] = "string changed" # we can change

print(my_list)

# a list can contain lists & tuples too
		#        __________________________________________
		# index |________0___________|_1_|_________2_______|
		#		|__0_|_1_|___2_______|_0_|___0_|_1_|___2___|
my_big_list = [ ["is","a","big_list"], 5, ("is","a","tuple") ]
print(my_big_list[0][2]) # --> big_list
