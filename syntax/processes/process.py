#!/usr/bin/env python

from multiprocessing import Process
from multiprocessing import Queue
from multiprocessing import Pipe

def fun(name):
	print "processing process"
	print "putting items in queue"
	queue.put([1,2,3])
	print "sending data in pipe"
	child_pipe.send("42")

if __name__ == '__main__':
	print "creating a process, queue and pipe"
	process = Process(target=fun, args=('Naidu',))
	queue = Queue()
	mother_pipe, child_pipe = Pipe()
	print "forking a process"
	process.start()
	print queue.get()
	print mother_pipe.recv()
	print "waiting for process to join"
	process.join()
	print "process join completed"
