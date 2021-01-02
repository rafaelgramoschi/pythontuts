"""

	Loops
	while, for, nested

"""
condition = True
while condition:
	# code
	print("While True print this")
	condition = False

count=0
while (count < 5):
	print("While count<5 print: " + str(count) )
	count+=1

print("Guess Game!! Guess computer number (it is 13)")
input=13
while(input!=13):
	if input<13:
		print("Input too small!")
	elif input>13:
		print("Input too big!")
	elif input==13:
		print("You win!")
	else:
		print("Wrong input! Try again!")

print("\nPrint fruits from list.")
fruits = ['banana', 'apple', 'orange']
for fruit in fruits:
	# code
	print(fruit)
	
print("\nLet's calculate factorial of the number 5.")


print("For loop with range(2)")
for i in range(2): #0,1
	print(i)
	
print("\nRange(2,5)")
for i in range(2,5): #2,3,4
	print(i)

"""

	break exit iteration
	continue continue to next iteration
	pass used as 'do nothing'

"""

print("\nfor i in range(0,5), break if i==2:")	
for i in range(0,5):
	print(i)
	if(i==2):
		break

print("\nfor a in range(0,5), continue if a==1")		
for a in range(0,5):
	if(a==1):
		continue
	print(a)
	
		
print("\npass is used to do nothing")
for item in ['ban','tan','pan']:
	pass
""" pass is used here, to do nothing
	in python an indentation is required,
	so python can understand that the for loop is ended
"""
