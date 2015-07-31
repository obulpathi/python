import gc
from memory_profiler import profile

@profile(precision=3)
def my_func():
    gc.set_debug(gc.DEBUG_LEAK)
    a = [1] * (10 ** 7)
    b = [1] * (10 ** 4)

    del a
    del b
    gc.collect()
    print("Garbage: ".format(gc.garbage))

print("Garbage collection enabled: {}".format(gc.isenabled()))
my_func()
my_func()
my_func()
