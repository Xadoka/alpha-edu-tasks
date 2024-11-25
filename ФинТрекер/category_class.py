class Category:
	def __init__(self,name):
		self.name = name


	def __str__(self): #! Для представления объекта
		return f'Category name: {self.name}'
