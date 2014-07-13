class Hi():
	x = 0

	def __repr__(self):
		return repr(self.x)

	def __cmp__(self, hi):
		if isinstance(hi, Hi):
			return self.x > hi.x

	def __len__(self):
		return 1

	def __delitem__(self, key): 
		del self.data[key]

h1 = Hi()
h2 = Hi()
h3 = Hi()

h1.x = 2
h2.x = 4
h3.x = 6

if h2 > h1:
	print("h2 > h1")

if h3 > h2:
	print("h3 > h2")

if h1 > h3:
	print("h1 > h3")
else:
	print("h1 <= h3")
