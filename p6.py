class Rectangle:
    def __init__(self,width,hight):
        self.width=width
        self.hight=hight
    def area(self):
        return self.width*self.hight
    def perimeter(self):
        return 2*(self.width+self.hight)
    def is_square(self):
        return self.width==self.hight
    def __str__(self):
        return f"rectangle({self.width}*{self.hight})"
          
r=Rectangle(4,6)
print(r,r.area(),r.perimeter(),r.is_square())
r1=Rectangle(5,5)
print(r1.is_square())

        