import time

ten_things = "Apples Oranges Crows Telephone Light Sugar"


print("Wait there are not 10 things in that list.  Let's fix that.")
time.sleep(1)

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
			  "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print("Adding: ", next_one)
	time.sleep(1)
	stuff.append(next_one)
	print(f"There are {len(stuff)} items now.")
	time.sleep(1)
	
print("There we go: ", stuff)
time.sleep(1)

print("Let's do some things with stuff.")
time.sleep(1)

print(stuff[1])
time.sleep(1)
print(stuff[-1]) # whoa! fancy
time.sleep(1)
print(stuff.pop())
time.sleep(1)
print(' '.join(stuff))
time.sleep(1)
print("#".join(stuff[3:5]))
time.sleep(1)
quit()