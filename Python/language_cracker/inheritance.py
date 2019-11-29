class Polygon():

    def __init__(self,n):
        self.sides = n
        
    def find_area(self):
        pass
    
    def __str__(self):
        return '{0} has {1} sides'.format(self.__class__.__name__,self.sides)

class Triangle(Polygon):

    def __init__(self,height,base):
        Polygon.__init__(self,3)
        self.height = height
        self.base = base

    def find_area(self):

        return 0.5*self.base*self.height

    

class Rectangle(Polygon):

    def __init__(self,length,breadth):
        Polygon.__init__(self,4)
        self.length = length
        self.breadth = breadth
    def find_area(self):
        return self.length*self.breadth


if __name__=="__main__":

    triangle = Triangle(3,4)
    print(triangle.find_area())
    print(triangle)

    rect = Rectangle(3,4)
    print(rect.find_area())
    print(rect)

    

