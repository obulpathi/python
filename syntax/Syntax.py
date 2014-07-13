#!/usr/bin/env python

# variables, strings, lists, ... 
x = 2.3
greeting = "Hi! How are you doing?"
fruits = ["Apple", "Bananna", "Cucumbar"]

x = 2
# if
if x == 2:
	print("x is 2")

# if else
if x == 2:
	print("x is 2")
else:
	print("x is not 2")

# if elif else
if x == 2:
	print("x is 2")
elif x == 3:
	print("x is 3")
else:
	print("x is not 2 and not 3")

print 'enter x'
x = input()
# for 

code = "x = 'this is fun'"

exec code
print code
