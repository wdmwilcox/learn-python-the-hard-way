def add(a, b):
	print(f"ADDING {a} + {b}")
	return a + b
	
def subtract(a, b):
	print(f"SUBTRACTING {a} + {b}")
	return a - b

def multiply(a, b):
	print(f"MULTIPLYING {a} + {b}")
	return a * b
	
def divide(a, b):
	print(f"DIVIDING {a} + {b}")
	return a / b

print("Let's do some math with functions.")

age = add(30, 6)
height = subtract(78, 8)
weight = multiply(77, 2)
iq = divide(280, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway
print("Here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
