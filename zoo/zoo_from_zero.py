class Animal:
	def __init__(self,name:str, species:str, age: int, is_endangered=None):
			self.name = name
			self.species = species
			self.age = age
			self.is_endangered = is_endangered or False

	def make_sound(self):
		pass

	def eat(food):
		pass

	def sleep(self):
		pass

class Lion(Animal):
	def __init__(self, name, species, age, is_endangered=None):
		super().__init__(name, species, age, is_endangered)
		self.speed = 80
	
	def make_sound(self):
		print(f'{self.name} just brrrrrrr')

	def hunting(self):
		print(f'{self.species} is hunting')

	def __str__(self):
		return f'{self.name} , {self.species}'

class Zebra(Animal):
	def __init__(self, name, species, age, is_endangered=None):
		super().__init__(name, species, age, is_endangered)
		self.stripes = True

	def make_sound(self):
		print(f'{self.name} just feeeer')

	def knock(self):
		print(f'{self.species} beat with leg')

class Pantera(Animal):
	def __init__(self, name, species, age, is_endangered=None):
		super().__init__(name, species, age, is_endangered)
		self.country = "Wakanda"

	def make_sound(self):
		print(f'{self.name} meaw')

	def speedrun(self):
		print(f'{self.species} run like a flash')


# 	def test_display(self):
# 		print(self.name)
# 		print(self.age)
# 		print(self.species)
# 		print(self.is_endangered)

#? 1
test_lion_object = Lion(name = "Alex", species="Lion", age=5)
test_lion_object2 = Lion(name = "Mufasa", species="Lion",age=3, is_endangered=True)

#? 2
test_zebra_object = Zebra(name="Dark", species="zebra", age = 4)
test_zebra_object.knock()

#? 3
test_pantera_object = Pantera(name="Black", species="pantera",age="5")
test_pantera_object.speedrun()

# test_lion_object.make_sound(
# )
# test_lion_object.hunting()

# test_lion_object.test_display()
# test_lion_object2.test_display()

class Exhibit:
	def __init__(self, name, location):
		self.name = name
		self.location = location
		self.animals_list = []

	def add_animal(self,animal_obj:Animal):
		self.animals_list.append(animal_obj)
		print(f'{animal_obj.species} with name {animal_obj.name} is added to {self.name}')

	def remove_animal(self,animal_obj:Animal):
		if animal_obj in self.animals_list:
			self.animals_list.remove(animal_obj)
		else:
			print('Nu such animal found')

	def show_animal(self):
		for animal in self.animals_list:
			print(animal)

#?Test exhibit
exhibit_for_lions = Exhibit(name='Lions EXH' , location="Turan")
exhibit_for_lions.add_animal(test_lion_object)
exhibit_for_lions.add_animal(test_lion_object2)

print(exhibit_for_lions.show_animal())

exhibit_for_lions.remove_animal(test_lion_object2)

print(exhibit_for_lions.show_animal())

class Staff:
	def __init__(self, name, position,age):
		self.name = name
		self.position = position
		self.age = age
	
	def work(self):
		pass
	
	def report(self):
		print(f'{self.name} is reporting')

class Zookeeper(Staff):
	def __init__(self, name, age):
		super().__init__(name, "Zookeeper", age)

	def work(self):
		print(f'{self.name} is taking care')

	def feed_animal(self, animal_obj: Animal):
		print(f'{self.name} is feeding {animal_obj.name}')

class Vet(Staff):
	def __init__(self, name, age):
		super().__init__(name, "Vet", age)

	def work(self):
		print(f'{self.name} is checking the health')

	def check_health(self, animal_obj:Animal):
		print(f'{self.name} is checking the health of {animal_obj.name}')

#?Test staff
zookeper = Zookeeper("Aina", 30)
vet = Vet("Askar", 50)

class Zoo:
	def __init__(self):
		self.exhibits = []
		self.staff_list = []

	def add_exhibit(self, exhibit_obj: Exhibit):
		self.exhibits.append(exhibit_obj)
		print(f"Exhibit {exhibit_obj.name} has been added")

	def add_staff(self, staff_obj: Staff):
		self.staff_list.append(staff_obj)
		print(f'Staff member {staff_obj.name} has been joined')

	def daily_oper(self):
		print("Starting daily oper: ")
		for staff in self.staff_list:
			staff.work()

zoo = Zoo()
zoo.add_exhibit(exhibit_for_lions)
zoo.add_staff(zookeper)
zoo.add_staff(vet)

zoo.daily_oper()

zookeper.feed_animal(test_lion_object)
vet.check_health(test_zebra_object)