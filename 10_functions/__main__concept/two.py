# when we import, all the code inside that imported module gets executed
import one
#																	 |||
#and after the import all the code inside this file will be executed vvv


print("top-level in two.py")

one.func()

print("[2] two.py name:" + __name__)

if __name__ == "__main__":
	print("[two.py] had been launched directly.")
else:
	print("[two.py] had been imported into another module")
