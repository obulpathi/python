#!/usr/bin/env python

import threading
from time import sleep 

class print_nums(threading.Thread):
	def run(self):
		for i in range(5):
			print i
		print "lets wait for fun"
		sleep(10)
		print "Finished printing numbets up to 5"

background = print_nums()

background.start() # start the main program
print "The main program continues to run in foreground."

background.join()    # Wait for the background task to finish
print "Main program waited until background was done."
