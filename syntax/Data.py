#!/usr/bin/env python

def odd(x):
	return x%2

li = range(10)
evensq = [x * x for x in li if odd(x)]
print(evensq)

print((lambda x:x*x)(2))
