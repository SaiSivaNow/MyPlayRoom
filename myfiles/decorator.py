


def a(func):

    def  wrapper(a,b):
        print(a+b)
        func(a,b)
        print(a-b)
    return wrapper


@a
def b(a,b):
    print(a*b)


        
