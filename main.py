class Rectangle:
    def __init__(self,width ,height):
        self.height=height
        self.width=width
    def area(self):
        area=self.height*self.width 
        print(area)
ractangel1=Rectangle(20,50)           
ractangel1.area()