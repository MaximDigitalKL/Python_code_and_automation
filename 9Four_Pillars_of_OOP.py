''' ABSTRACTION
Abstract Class: GeometricForm
It contains one field: PI=3.14
It contains one abstract method:  area()
It contains a description method: it prints on the screen: "Most likely I have corners" '''
from abc import abstractmethod


class GeometricForm:
    pi = 3.14

    @abstractmethod
    def area(self):
        pass

    def description(self):
        print(f'Most likely I have corners')

'''INHERITANCE
Class Square - inherits from GeometricForm
Constructor for side
'''

'''ENCAPSULATION
side -  is privet property
implement getter setter deleter for side
implement the abstract method requested by the interface
'''
class Sqaure(GeometricForm):
    __side = None

    def __init__(self,side):
        self.__side = side

    @property
    def side(self):
        pass
    @side.getter
    def side(self):
        return self.__side

    @side.setter
    def side(self,side):
        self.__side = side

    @side.deleter
    def side(self):
        self.__side = None

    def area(self):
        area = pow(self.__side,2)
        return area

    '''POLIMORPHISM
    Define a new description method -  print "I don't have corners"
    Create an object and run through it's methods
    '''

    def new_description(self,corners = 0):
        if corners == 0:
            print(f"I don't have corners")
        else:
            print(f'I have {corners} corners')

square1 = Sqaure(6)
square1.description()
square1.new_description(4)
print(f'The side of the square is {square1.side}')
square1.side = 8
print(f'The new side of the square is: {square1.side}')
del square1.side
print(f'Side of the square after deleter: {square1.side}')
square1.side = 6
print(f'The area of the square is: {square1.area()}')

'''
Clasa Cerc - inherits GeometricForm
constructor for radius
radius is private property
implement getter setter deleter for radius
implement the abstract area method, and use PI from the GeometricForm
'''
print ('-----------------------------------')
class Circle(GeometricForm):
    __radius = None

    def __init__(self,radius):
        self.__radius = radius

    @property
    def radius(self):
        pass

    @radius.getter
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    @radius.deleter
    def radius(self):
        self.__radius = None

    def area(self):
        area = self.pi * pow(self.__radius,2)
        return area

    def new_description(self,corners = 0):
        if corners == 0:
            print(f"I don't have corners")
        else:
            print(f'I have {corners} corners')

circle1 = Circle(5)
circle1.description()
circle1.new_description()
print(f'The radius of the circle is {circle1.radius}')
circle1.radius = 10
print(f'The new side of the circle is: {circle1.radius}')
del circle1.radius
print(f'Side of the circle after deleter: {circle1.radius}')
circle1.radius = 6
print(f'The area of the circle is: {circle1.area()}')
