
class Employee():
    
    #name = "Teja"
    company = "Mindtree"
    mail = "teja463@gmail.com"
    
    __sal = 22000
    
    def __init__(self):
        self.name = "Pramod"

    def getSal(self):
        return self.__sal
    
obj1 = Employee()

#print (Employee.name)
print (obj1.name)
print (obj1.getSal())
print (obj1._Employee__sal)

# Inheritance

    
class Parent():
    def __init__(self):
        print ("In parent")

class Child1(Parent):
    def __init__(self):
        print ("In child1")

class Child2(Parent):
    def __init__(self):
        print ("In child2")

class GrandChild(Child2, Child1):
    pass
    """def __init__(self):
        print ("In grandchild")"""
        
grand_child = GrandChild()
child1 = Child1()



# Documentation

class Sample():
    """
    This is the documentation in multiple lines
    """
    "" 
    pass

sample = Sample()
print (sample.__doc__)
