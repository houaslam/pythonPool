import sys;


system_argument = sys.argv
error_msg = ""
try:
	
	if len(system_argument) > 2:
		raise AssertionError()
	argument = int(system_argument[1])
	if argument % 2 == 0:
		print("I'm Even.")
	else: print("I'm Odd.")
except ValueError as e:
	print(f"AssertionError: argument is not an integer")
except AssertionError as e:
	print(f"AssertionError: more than one argument is provided")
