#!/usr/bin/env python

def fib1(n):
	x, y  = 0, 1
	while n > 0:
		x, y = y, x+y
		n = n - 1
	return y

def fib2(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fib2(n-1) + fib2(n-2)
