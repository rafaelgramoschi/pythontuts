"""
	Strings methods
"""

str = "yo soy pablo"
print( str.capitalize() ) # Yo soy pablo
str.count("y", 0, len(str) ) # counts how many times "y" occurs from pos 0 to end of string
s = str.encode('utf-8', 'strict') # returns encoded string version of str
print(s)

max(str) # order of letters: abcdefg... min is a max is z
min(str) # this methods count based on ASCII code, anyway it's easy

# str.replace(what, intoWhat, occurences)
# if occurences is not specify, it will replace all the occurences
str.replace('o','-o-',1) # replace first 'o' with '-o-
str.upper() # str to uppercase

str.index('p') # return index value of 'p', if not present raise exception
str.find('L') # return index value, if not present returns -1
