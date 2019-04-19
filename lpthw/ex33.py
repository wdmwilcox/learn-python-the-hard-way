def make_sized_list(inp):

	i = 0
	numbers = []

	while i < inp:
		print(f"At the top i is {i}")
		numbers.append(i)
		
		i += 1
		print("Numbers now: ", numbers)
		print(f"At the bottom i is {i}")

	print("The numbers: ")

	for num in numbers:
		print(num)

inp = int(input("Enter an integer: "))
make_sized_list(inp)