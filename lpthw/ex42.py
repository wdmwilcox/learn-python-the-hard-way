# animal is a class of type object
class Animal(object):
	pass
	
# dog is-a class of type animal
class Dog(Animal):
	
	def __init__(self, name):
		# dog has-a attribute name
		self.name = name

# cat is-a class of type animal		
class Cat(Animal):

	def __init__(self, name):
		# cat has-a attribute name
		self.name = name
		
# person is-a class of type object
class Person(object):
	
	def __init__(self, name):
		# person has-a attribute name
		self.name = name
		
		# Person has-a attribute pet
		self.pet = None
		
		
class Employee(Person):
	
	def __init__(self, name, salary):
		super(Employee, self).__init__(name)
		self.salary = salary
		
# class fish is-a class of type object
class Fish(object):
	pass
	
class Salmon(Fish):
	pass
	
class Halibut(Fish):
	pass
	

rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()


