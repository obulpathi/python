class Error1(Exception):
	pass

class Error2(Exception):
	pass

def fun(x):
	if x == 1:
		raise Error1
	if x == 2:
		raise Error2

print('trying try catch')
try:
#	fun(1)
	fun(2)
except Error1:
	print('hey got error1')
except Error2:
	print('hey got error2')
