# imports


# global variables


# classes


class Room(object):
	
	
	def __init__(self, room_name, enter_dialogue, cleaned_dialogue, item_list):
		self.room_name = room_name
		self.enter_dialogue = enter_dialogue
		self.cleaned_dialogue = cleaned_dialogue
		self.item_list = item_list
		self.is_cleaned = bool(False)
		
	
class Player(object):

	def __init__(self, player_name):
		self.player_name = player_name


class Item(object):

	def __init__(self, item_name):
		self.item_name = item_name
			
	
class Engine(object):

	
	def __init__(self, player_name):
		self.player_name = player_name
		pass
	
	def get_next_room(self):
		self.room_input = input("Where would you like to go? : ")
		if room_input in rooms:
			next_room = rooms[room_input]
			return next_room
		else:
			print("That room's not ready yet.")
			get_next_room()
			pass
	

	def enter_room(self, room):
		if room.is_cleaned:
			print(room.cleaned_dialogue)
			pass
		else:
			print(room.enter_dialogue)
			room_item_list = []
			for item in room.item_list:
				room_item_list.append(Item(item))
			for item in room_item_list:
				print(item.name)
				print(item.is_cleaned)
			
				
	def play(self):
	
		bedroom = Room('bedroom', 'This bedroom is a mess; I wouldn\'t want to sleep here!',
				   'This is a great place to sleep and get dressed.',['bed','dresser','closet'])
		kitchen = Room('kitchen', 'The dangerous kitchen; if it\'s not one thing it\'s another.',
				   'I can\'t wait to cook in this kitchen!',['sink','oven','counter'])
		living_room = Room('living room', 'This living room is literally killing me!',
					   'This is an epic place to live.',['couch','bookshelf','entertainment center'])
		rooms = {'bedroom' : bedroom, 
			 'kitchen' : kitchen,
			 'living room' : living_room
			 }
			 
		won = False
		
		self.get_next_room()
		
		print("Your house is a mess.  You alone can clean it.")
		print("The bedroom, kitchen, and living room are messy.  Where do you start?")
		while won is False:
			
			enter_room(next_room)			
		

def main():
	
	print('Welcome, adventurer.  Your quest is to clean your house.')
	player_name = input('What be your name? > ')
	game = Engine(player_name)
	game.play()
	exit(0)


if __name__ == main():
	main()

	
	