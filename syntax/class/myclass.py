#!/usr/bin/env python

print "welcome to the world of classes"

class animal():
	name = "animal"
	
	def describe(self):
		print "Something that can animate"

class mammal(animal):
	name = "mammal"

	def describe(self):
		print "females have mammary glands"

anime = animal()
anime.describe()
print anime.name

bat = mammal()
bat.describe()
print bat.name
