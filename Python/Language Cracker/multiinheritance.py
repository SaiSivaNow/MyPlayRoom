

class A():
    def __init__(self):
        self.name = self.__class__.__name__

    def methodA(self):
        print('methodA')

class B():

    def __init__(self):
        self.name = "B"

    def methodB(self):
        print('methodB')


class C(A,B):

    def __init__(self):
        B.__init__(self)

    def methodC(self):
        self.methodA()
        self.methodB()
        print(self.name)
    

c = C()
c.methodC()
