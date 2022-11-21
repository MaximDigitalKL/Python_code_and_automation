'''1.Function that returns the sum of two numbers'''
def calculator(a,b):
    sum = a+b
    return sum

#no1 = int(input("Insert first number: "))
#no2 = int(input("Insert second number: "))
print(f'Sum of numbers is {calculator(1,2)}') #print(f'Sum of numbers is {calculator(no1,no2)}')

'''2. Function that return TRUE if the number is even and FALSE if it's odd'''
def even(x):
    even = False
    if x % 2 == 0:
     even = True
    return even

print(f'Is the number even ? {even(10)}')

'''3. Function that returns the total number of characters of you name.'''
def number_of_characters(last_name, frist_name):
    return len(last_name) + len(frist_name)
#last_name=input('Insert your last name: ')
#first_name=input('Insert your first name: ')

print(f'Your name has {number_of_characters("Maxim","Razvan")} characters')


'''4. Function that returns the area of a Right Angle'''
def area_ra(W,L):
    area = W*L
    return area

print(f'The Right Angle has an area of {area_ra(5,10)} squared centimeters')

'''5. Function that returns the area of a circle'''
def area_circle():
    #radius=int(input("Insert circle radius:"))
    radius = 4
    pi = 3.14
    area_circle = radius*pi
    return area_circle

print(f'The circle has an area of {area_circle()} squared centimeters')

'''6. Function that returns True if a character exists in a string and False if it doesn't'''
def True_false():
    yes_or_no = False
    sentence = "Wise guys all over Chicago"
    #x = input("Guess a letter from the secret phrase: ")
    x = "a"
    if x in sentence:
        yes_or_no = True
    return yes_or_no

print(f'Did I guess right ? {True_false()} ')


'''7. Function without return that prints on screen:
- number of lower case characters (x)
- number of upper case characters (y)'''
def big_or_small ():
    lower_case = 0
    upper_case = 0
    string = "fgHYTdfGHJtrFGhjKu"
    for i in range(0,len(string)):
        if string[i].isupper():
            upper_case += 1
        else:
            lower_case += 1
    print(f'Number of lower case characters is: {lower_case}')
    print(f'Number of upper case characters is: {upper_case }')
big_or_small()

'''8.Function that gets a list and returns a new list only with positive numbers'''
def positive_numbers(list):
    positive_list = []
    i = 0
    while i < len(list):
        if list[i] >= 0:
            positive_list.append(list[i])
        i += 1
    return positive_list

full_list = [-5,6,8,-7,-6,3,2,0,-4,-9]
print(positive_numbers(full_list))

'''9. Function gets 2 numbers, prints on screen (no return)
- first number x is greater than second number y
- second number y is greater than first number x
- the numbers are equal'''
def big_small(no1, no2):
    if no1 > no2:
        print(f'First number {no1} is greater than second number {no2}')
    elif no2 > no1:
        print(f'Second number {no2} is greater than first number {no1}')
    else:
        print(f'Numbers {no1} and {no2} are equal')
big_small(4, 6)

'''10. Function that gets a set of numbers
- print: I have added a new number in set, return True
- print: I did not add the number in set, it already exists, return False'''
def nr_in_set(set):
    #number = int(input('Insert a number: '))
    number = 5
    maybe = True
    if number in set:
        maybe = False
        print(f'I did not add the number in set, it already exists')
    else:
        set.add(number)
        print(f'I have added a new number in set')
    return maybe

set = {1,4,6,7,3}
print(nr_in_set(set))

'''11. Function that gets a month and returns how many days that month has'''
def days_of_the_month(month):
    list1={"January", "March", "May", "July", "August", "October", "December"}
    list2={"April", "June", "September", "November"}
    if month in list1:
        days = 31
    elif month in list2:
        days = 30
    else:
        days = 28
    return days
month = "February"
print(f'The month of {month} has {days_of_the_month(month)} days')

'''12.Function that returns 4 values: sum, diff, multiplication and division'''
def mathematical_calculus(a, b):
    sum = a+b
    difference = a-b
    multiplication = a*b
    division = a/b
    return sum, difference, multiplication, division

sum, dif, mult ,div = mathematical_calculus(2,6)
print(f'The sum is: {sum}')
print(f'The difference is: {dif}')
print(f'The product is: {mult}')
print(f'The quotient is: {div}')

'''13. Function that receives a list of numbers (from 0 to 9)
Eg: [1, 3, 1, 5, 9, 7, 7, 5, 5]
It returns a dictionary that tells us how many times a number appears in the list
eg: => dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
} '''
def count(list):
    dict = {}
    for i in range(len(list)-1):
        count = list.count(list[i])
        dict[list[i]] = count
    return dict

list = [1,3,1,5,9,7,7,5,5]
print(count(list))

'''14.Function that gets 3 numbers, returns the biggest value '''
def the_biggest_number(a, b, c):
    return max(a,b,c)

#no1=int(input(f'Insert first number: '))
#no2=int(input(f'Insert second number: '))
#no3=int(input(f'Insert third number: '))
#print(the_biggest_number(no1,no2,no3))
print(f'The biggest number is {the_biggest_number(5, 6, 7)}')

'''15. Function that receives a number and returns the sum of all numbers from 0 to that number
Eg: for nr 3 the sum will be 6 (0+1+2+3)'''
def sum_of_all(number):
    sum = 0
    i = 0
    while i <= number:
        sum += i
        i += 1
    return sum
number =int(input(f'Insert number: '))
print(f'Sum of numbers from 0 to {number} is {sum_of_all(number)}')

'''16. Function that gets 2 lists, it returns the common elements
Eg:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
answer: {2, 3}'''
from datetime import datetime, timedelta, date


def union(list1, list2):
    i = 0
    j = 0
    common={20}
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                common.add(list1[i])
    common.remove(20)
    return common
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
print(f'The common elements are: {union(list1, list2)}')

'''17. Function that applies a price reduction
eg: price 100, discount 10%....new price 90
treat also cases where discount is invalid, eg discount of 110%'''
def deduction(price, discount):
    percentage = (price * discount) / 100
    new_price=0
    if percentage > price:
        print(f'invalid discount')
    else:
        new_price= price - percentage
    return new_price
price=int(input("Insert product price: "))
discount=int(input("insert % discount: " "%"))
print(deduction(price, discount))

'''18. Function to show the current date and time in Romania
Also to show the current date and time in China'''
def date_and_time():
    ro= datetime.now()
    china= datetime.now() + timedelta(hours=6)
    print(f'Current date and time in Romania is: {ro}')
    print(f'Current date and time in China is: {china}')
date_and_time()

'''19. Function to show how many days are left until your birthday'''
def countdowntoPARTY():
    count_down=date(2023,3,2)-date.today()
    print(f'Until my birthday there are {count_down.days} days left')
countdowntoPARTY()
