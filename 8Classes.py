'''1.Class Circle
Atributes: radius, colour
Constructor: both atributes
Methods:
● describe_circle() - it will print radius and colour
● area() - it will return area
● diameter() with return
● circumferince() with return'''
from tabulate import tabulate


class Circle:
    radius = None
    colour = None

    def __init__(self, radius, colour):
        self.radius = radius
        self.colour = colour

    def describe_circle(self):
        print(f'The colour of the circle is: {self.colour}')
        print(f'The radius of the circle has: {self.radius} cm')

    def area(self):
        pi = 3.14
        a = pi*(self.radius ** 2)
        return a

    def diameter(self):
        d = 2*self.radius
        return d

    def circumferince(self):
        pi = 3.14
        c = pi*(2 * self.radius)
        return c


circle1 = Circle(6, "verde")
circle1.describe_circle()
print(f'Circle area has: {circle1.area()} sq-cm')
print(f'Circle diameter has: {circle1.diameter()} cm')
print(f'Circle circumferince is: {circle1.circumferince()} cm')
print("-------------------------------------")

'''2. Class Right_Angle
Atributes: length, width, colour
Constructor: all atributes
Methods:
● description()
● area()
● perimeter()
● Change_colour(new_colour) - no return for this method.
check the method by re-running the describe method.'''

class Right_angle:
    length = None
    width = None
    colour = None

    def __init__(self,lungimea, latime, culoare):
        self.length = lungimea
        self.width = latime
        self.colour = culoare

    def description(self):
        print(f'The Right Angle has a length of  {self.length} cm, a width of {self.width} cm and the colour {self.colour}')

    def area(self):
        a = self.length * self.width
        return a

    def perimeter(self):
        p = (2 * self.length) + (2 * self.width)
        return p

    def Change_colour(self, new_colour):
        self.colour = new_colour

right_angle1 = Right_angle (10, 3, "green")
right_angle1.description()
print(f'Right Angle area is: {right_angle1.area()}')
print(f'Right Anfle perimeter is: {right_angle1.perimeter()}')
right_angle1.Change_colour("red")
right_angle1.description()
print("-------------------------------------")

'''3. Class Employee
Atributes: last_name, first_name, salary
Constructor: all atributes
Methods:
● Description()
● Full_name()
● Monthly_salary()
● Annual_salary()
● salary_increase(percentage)'''

class employee:
    last_name = None
    first_name = None
    salary = None

    def __init__(self, last_name, first_name, salary):
        self.last_name = last_name
        self.first_name = first_name
        self.salary = salary

    def description(self):
        l1=[["Employee last name", "Employee first name", "Employee salary"], [self.last_name, self.first_name, self.salary]]
        print(tabulate(l1, headers="firstrow", tablefmt="psql"))

    def Full_name(self):
        print(f'Employees full name is: {self.last_name} {self.first_name}')

    def Monthly_salary(self):
        print(f'Employees monthly salary is: {self.salary} RON')

    def Annual_salary(self):
        sa = 12*self.salary
        return sa

    def Salary_increase(self, percentage):
        print(f'The employee gets a raise of  {percentage} %')
        self.salary += (self.salary * percentage) / 100
        print(f'Salary after raise is: {self.salary}')

angajat1 = employee("Maxim", "Razvan", 4700)
angajat1.description()
angajat1.Full_name()
angajat1.Monthly_salary()
print(f'Employees  {angajat1.last_name} {angajat1.first_name} has an annual salary of {angajat1.Annual_salary()}')
angajat1.Salary_increase(10)
print("-------------------------------------")

'''4.Class Bank_Account
Atributes: iban, account_holder, amount
Constructor: all atributes
Methods:
● show_balance() - Account holder x has in account y the amount of z RON
● debit_account(amount)
● credit_accout(amount)'''

class Bank_account:
    iban = None
    account_holder = None
    balance = None

    def __init__(self, iban, account_holder, balance):
        self.iban = iban
        self.account_holder = account_holder
        self.balance = balance

    def Show_balance(self):
        print(f'Account holder {self.account_holder}has in account {self.iban} the amount of {self.balance} RON')

    def debit_account(self, amount):
        print(f'Your account has been debited with {amount} RON')
        self.balance += amount
        print(f'Current balance is: {self.balance}')

    def Credit_account(self, amount):
        print(f'Your acoount has been credited with {amount} RON')
        self.balance -= amount
        print(f'Current balance is: {self.balance}')

account1= Bank_account("ROBTRL19900302654987", "Maxim Razvan", 10000)
account1.Show_balance()
account1.debit_account(999)
account1.Credit_account(555)

'''5. Clasa Invoice
Atributes: series (it will be constant, no constructor, all invoices will have the same series),
 number, product name, quantity, unit_price
Constructor: all atributes without the series
Methods:
● change quantity(quantity)
● change price(price)
● change product name(name)
● generate invoice() - table format
invoice series x number y
date: automatically generated
product | quanitty | unit price | total
Phone | 7 | 700 | 49000'''
from datetime import date, datetime

from tabulate import tabulate


class Invoice:
    series = "CJ"
    number = None
    product_name = None
    quantity = None
    unit_price = None

    def __init__(self, number, product_name, quantity, unit_price):
        self.number = number
        self.product_name = product_name
        self.quantity = quantity
        self.unit_price = unit_price

    def change_quantity (self, quantity):
        self.quantity = quantity

    def change_price (self, price):
        self.unit_price = price

    def schimba_nume_produs (self, name):
        self.product_name = name

    def generate_invoice(self):
        print(f'Invoice series: {self.series} number: {self.number}')
        print(f'Invoice Date: {datetime.now()}')
        table= [['Product', 'Quantity', 'Unit Price', 'Total'],
                [self.product_name, self.quantity, self.unit_price, self.quantity * self.unit_price]]
        print(tabulate(table, headers="firstrow", tablefmt="psql"))


Product1 = Invoice(12564, "Samsung Note 20", 6, 4800)
Product1.change_quantity(10)
Product1.change_price(5600)
Product1.schimba_nume_produs("Samsung Galaxy S22 Ultra")
Product1.generate_invoice()

print ("-----------------------------------------------------------------")


'''6.Class Car
Atributes: brand, model, max_speed, current_speed, colour,
available_colours (set), registered (bool)
colour = grey - all cars come out of the factory grey
current_speed = 0 - all cars have 0 speed when they leave the factory
available colours = pick 5 to 7 colours
brand = pick a brand - the factory makes only 1 brand but multiple models
registered = False
Constructor: model, max_speed
methods:
● description() - print all atributes except the available colours
● registered() - it will change the atribute to True
● paint(colour) - only if the new colour is within the available colours set, otherwise it will print an error message
● accelerate(speed) - it will accelerate to a certain speed, if speed is negative (error messsage)
if speed is greater than max_speed, the car will cap out at max speed.
● break() - the car will break to 0'''

class Car:
    Brand = "BMW"
    Model = None
    max_speed = None
    current_speed = 0
    colour = "grey"
    available_colours = {"red", "yellow", "blue", "black", "rainbow"}
    registered = False

    def __init__(self, model, max_speed):
        self.Model = model
        self.max_speed = max_speed

    def description(self):
        print(f'Brand: {self.Brand}\n'
              f'Model: {self.Model}\n'
              f'Max speed: {self.max_speed} KM/H\n'
              f'Current speed: {self.current_speed} KM/H\n'
              f'Colour: {self.colour}\n'
              f'Registered: {self.registered}')

    def registration(self):
        self.registered = True

    def re_painitng(self, colour):
        if colour in self.available_colours:
            self.colour = colour
        else:
            print(f'Colour {colour} is not in the available colour list')

    def accelerate(self, speed):
        if speed < 0:
            print(f'CPU error, speed can not be negative')
        elif speed > self.max_speed:
            self.current_speed = self.max_speed
        else:
            self.current_speed = speed

    def back_to_a_stand_still(self):
        self.current_speed = 0



car1= Car("M3", 280)
car1.description()
car1.registration()
car1.re_painitng("pink")
car1.re_painitng("rainbow")
car1.accelerate(320)
car1.back_to_a_stand_still()
car1.description()

print ("-----------------------------------------------------------------")

'''7. Class TodoList
Atributes: todo (dict, key is task name, value is task description)
in the begining there are no tasks, the dict is empty, no constructor needed
Methods:
● Add_task(task_name, description) - add to dictionary
● finalize_task(task_name) - remove from dictionary
● show_todo_list() - just the keys
● show additional details(task_name) - based on task name, print additional details
  - if task not in dict, ask if the user wants it to be added
  -if the answer is no - say good by
  -if the answer is yes- ask for additional details and add the task to the dict'''

class TodoList:
    todo = {
    }

    def add_task(self, task_name, description):
        self.todo[task_name] = description

    def finalize_task(self, task_name):
        self.todo.pop(task_name)

    def show_todo_list(self):
        print(self.todo.keys())

    def show_additional_information(self, task_name):
        if task_name in self.todo.keys():
            print(f'Additional information: {self.todo.get(task_name)} ')
        else:
            print(f'The entered task is not in the list.\n'
                  f'Do you want task {task_name} to be added ?')
            yes_no = input('Answwer with "yes" or "no": ')
            if yes_no == "yes":
               details= input("Provide additional details: ")
               self.todo[task_name] = details
            else:
                print(f'Good By !')



    def view(self):
        print(self.todo)

task_list1= TodoList()
task_list1.add_task("wash dishes", "with soap and spunge")
task_list1.add_task("cut grass", "with scythe")
task_list1.add_task("groceries_shopping", "milk, cheese, ham, eggs")
task_list1.add_task("sleep", "without snoring")
task_list1.view()
print ("-----------------------------------------------------------------")
task_list1.finalize_task("cut grass")
task_list1.view()
print ("-----------------------------------------------------------------")
task_list1.show_todo_list()
task_list1.show_additional_information("wash dishes")
task_list1.show_additional_information("cut fingernails")
task_list1.show_additional_information("make fries")
task_list1.view()

# 8. Improvisation
class House:
    number_of_stories = None
    number_of_rooms = None
    number_of_bathrooms = None
    construction_material = None
    square_footage = None
    year_of_construction = None
    address = None
    energetic_class = None
    price = None


    def __init__(self, number_of_stories, number_of_rooms, number_of_bathrooms, construction_material, square_footage, address):
        self.number_of_stories = number_of_stories
        self.number_of_rooms = number_of_rooms
        if number_of_bathrooms > 2:
            print("You can not have more than two bathrooms")
        else:
            self.number_of_bathrooms = number_of_bathrooms
        self.construction_material = construction_material
        self.square_footage = square_footage
        self.address = address

    def approval_for_number_of_stories(self):
        if self.number_of_stories > 5:
            print("In this area the maximum number of stories is 5")
        else:
            self.approval = True

    def year_of_construction_update(self, construction_year):
        self.year_of_construction = construction_year
        return self.year_of_construction


    def vinde_casa(self):
        print(f"House for sale on {self.address}"
                f"Number of rooms: {self.number_of_rooms}"
                f"Number of stories: {self.number_of_stories}"
                f"Number of bathrooms: {self.number_of_bathrooms}"
                f"Year of construction: {self.year_of_construction},"
                f"Square footage: {self.square_footage}"
                f"Building material: {self.construction_material}")

house1 = House(0, 1, 1, "concrete", 40, "Memory Lane 23")
house2 = House(0, 2, 1, "bricks", 70, "Boulevard of broken dreams")
House3 = House(1, 4, 2, "BCA", 130, "Via del mundo")
print(f"The first house has {house1.number_of_rooms} rooms")
print(f"The first house is built out of {house1.construction_material}")
print(f"First house addressis: {house1.address}")
print(f"Secodn house has {house2.number_of_bathrooms} bathrooms")
print(f"Square footage of the second house is {house2.square_footage} square feet")
print(f"Construction of the second house ended in  {house2.year_of_construction_update(2022)}")
House3.price = 150000
print(f"Price of house three is {House3.price} EURO")

