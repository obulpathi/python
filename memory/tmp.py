def profile4():
    process = Process(target=foo, args=('hi',))
    proc = psutil.Process(process.pid)
    mem0 = proc.get_memory_info().rss
    process.start()
    mem1 = proc.get_memory_info().rss
    process.join()
    mem2 = proc.get_memory_info().rss

    print "Initial: {0}".format(mem0/1000000.0)
    print "Running: {0}".format(mem1/1000000.0)
    print "Final: {0}".format(mem2/1000000.0)
    #import pdb; pdb.set_trace()
    #print 'hi'
