# open a terminal and run this file: python3 one.py, and see what happens
# then: python3 two.py

def func():
	print("[one.py] func() had been launched.")

print("top-level in one.py")

print("[1] one.py name:" + __name__)

## __name__ contains the value of __main__ when the file gets executed as main (python3 one.py in this case)
if __name__ == "__main__":
	print("[one.py] had been launched directly.")
else:
	print("[one.py] had been imported into another module")
