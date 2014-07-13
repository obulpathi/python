#!/usr/bin/env python

class one():
	x = 1

	def printx(self):
		print(self.x)
		self.__printx()
	
	def __printx(self):
		print('__printx')

	def __printx__(self):
		print('__printx__')


class two():
	y = 2

	def printy(self):
		print(self.y)

	def printx(self):
		print(self.y)


class three(one, two):
	pass

t = three()
t.printx()
#t.__printx()
t.__printx__()
t.printy()
