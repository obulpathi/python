def foo(x):
    print(x)
    def bar(y):
        x = 4
        print(x)
    bar(7)
    print(x)
foo(2)
