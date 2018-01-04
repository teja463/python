
class Shape():
    
    def __init(self):
        print ("Shape __init__")
    
    def draw(self):
        print ("Drawing a shape")

class Circle(Shape):
    pi = 3.14
    def __init__(self):
        print ("Circle __init__")

    def draw(self):
        
        print ("Drawing Circle")

    def cal_cirumference(self,radius=None):
        
        if radius is not None:
            return (2 * self.pi * radius)
        else:
            return 0.0

circle = Circle()
circle.draw()
print (circle.cal_cirumference(2))
print (circle.__class__)


class MyException(Exception):
    err_msg = "This is my exception"

try:
    name = input("Enter a name: ")
    if name!= "Teja":
        raise MyException
    else:
        print ("You are: ", name)
except (ZeroDivisionError, MyException) as e:
    print ("Caught exception", e.err_msg)

else:
    print ("All if in in try/except block")
finally:
    print ("All done")
