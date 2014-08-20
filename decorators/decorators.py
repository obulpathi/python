class Cat(object):
	""" the Cat """
	
	def __init__(self, name):
		self._name = name
	
	@property
	def name(self):
		print("getting name")
		return self._name
	
	@name.setter
	def name(self, name):
		print("setting name")
		self._name = name

	@name.deleter
	def name(self):
		print("deleting name")
		del self._name
		
cat = Cat("Billy")
print cat.name
cat.name = "Billy 2"
print cat.name
del cat.name
cat.name = "Billy 2"
print cat.name
