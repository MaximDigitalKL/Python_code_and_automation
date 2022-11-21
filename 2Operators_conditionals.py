#1 - Explain in your own words how if/else works:
# "If" for me works like a crossroads intersection, if the statement is true, we go to the right, if it is false we go to the left.
from random import randrange

x = int(input("Insert number x: "))

#2. Verify if x is a natural number.
if x >= 0 and type(x) == int:
    print(f' {x} is a natural number')
else:
    print(f' {x} is not a natural number')

#3. Verify if x is positive, negative or neutral.
if x > 0:
    print(f' {x} is positive')
elif x < 0:
    print(f' {x} is negative')
else:
    print(f' {x} is neutral')

#4. Verify and print if x is between -2 and 13
if x > -2 and x < 13:
    print(f'{x} is within interval (-2) / 13')
else:
    print(f'{x} is not within interval (-2) / 13')

#5 Verify and print if the difference between x and y is smaller than 5
y = 6 # float(input("Insert number y: "))
if abs(x-y) < 5:
    print(f'The difference between {x} and {y} is smaller than 5')
else:
    print(f'The difference between {x} and {y} is smaller not than 5')

#6. Verify if x is not within interval 5/27 -use NOT
if not(x > 5 and x < 27):
    print(f'{x} is not within interval 5 / 27')
else:
    print(f'{x} is within interval 5 / 27')

#7. Verify if x and y are equal, if nto print which is greater
if x == y:
    print(f'{x} and {y} are equal')
elif x > y:
    print(f'{x} is the greater number')
else:
    print(f'{y} is the greater number')

#8. x,y and z are the sides of a tirangle, verify if the triangle is equilateral, isosceles or scalene
z = 5
if x == y == z:
    print(f'equilateral triangle')
elif x == y or y == z or z == x:
    print(f'isosceles triangle')
else:
    print(f'scalene triangle')

#9. Read a letter from keyboard, specify if it is a vowel or not
lit = str(input("Insert a letter: "))
vowels = ['A', 'E', 'I', 'O', 'U']
if lit.upper() in vowels:
    print(f'The inserted letter is a vowel')
else:
    print(f'The inserted letter is a consonant')

#10. Transform and print the grades from Romanian format into American:
#                      Over 9 => A
#                      Over 8 => B
#                      Over 7 => C
#                      Over 6 => D
#                      Over 4 => E
#                      4 or under => F

grade = float(input("Insert grade: "))
if grade > 9:
    print(f'Your grade is A')
elif grade > 8:
    print(f'Your grade is B')
elif grade > 7:
    print(f'Your grade is C')
elif grade > 6:
    print(f'Your grade is D')
elif grade > 4:
    print(f'Your grade is E')
elif grade <= 4:
    print(f'Your grade is F')


number= int(input("Insert number: "))
#11 - verify if "number" has at least 4 digits
if len(str(number)) >= 4:
    print(f'The selected number has at least 4 digits')
else:
    print(f'The selected number has less than 4 digits')

#12. Verify if "number" has exactly 6 digits
if len(str(number)) == 6:
    print(f'The selected number has exactly 6 digits')
else:
    print(f'The selected number does not have 6 digits')

#13. Verify if "number" is odd or even
if (number % 2) == 0:
    print(f'The selected number is even')
else:
    print(f'The selected number is odd')

#14. Verify and display the greater number between: number, number_2 and number_3
number_2 = 8
number_3 = 6
if number > number_2 and number > number_3:
    print(f'{number} is the greater number')
elif number_2 > number and number_2 > number_3:
    print(f'{number_2} is the greater number')
else:
    print(f'{number_3} is the greater number')

#15. a,b and c are the angles of a triangle, print if it is a valid triangle
a = 40
b = 60
c = 90
if (a+b+c) == 180:
    print(f'It is a valid triangle')
else:
    print(f'The triangle is invalid')

#16. Given the string "Coral is either the stupidest animal or the smartest rock"
                # read from keyboard x
                # print the string without the last x characters
x= int(input("Insert number of missing characters: "))
prop = "Coral is either the stupidest animal or the smartest rock"
print(prop[0:-x])

#17. Same string. Print on screen a new string that is created from the first and last 5 charactes of the original.
print(f'{prop[0:6]}{prop[len(prop)-5:len(prop)]}')

#18. Same string.
                  # ● Save in a variable and print the index of the word "rock"
                  # ● Using this variable and slicing print the entire string up to the word "rock"
                  # ● output: 'Coral is either the stupidest animal or the smartest '
here = prop.index('rock')
print(prop[0:here])

#19. Read from keyboard a string:
                  # Check if the first and the last characters are the same regardless if they are upper or lower case.
                  # use the assert function

new = input("Insert string: ")
assert new[0].upper() == new[len(new)-1:len(new)].upper(), "First and last characters are not the same"

#20. Given the string: '0123456789'
                # ● Print only the odd numbers
                # ● Print only the even numberse

nr = "0123456789"
even = ""
odd = ""
for i in range (0,len(nr)):
 if int(nr[i]) % 2 == 0:
     even = even + nr[i]
 elif int(nr[i])  % 2 != 0:
     odd = odd + nr[i]
print(f'The even numbers are: {even}')
print(f'The odd numbers are: {odd}')

'''Game:  Guess the dice
* generate a random number - this will represent the throwing of the dice"
* the user will insert from keyboard his guess
Verify and print if the user guessed correctly
there are 3 options
● You lost! You picked a smaller number. You chose x but it was  y
● You lost! You picked a greater number. You chose x but it was  y
● You Win !. Congratulations! You chose x and the dice was y'''
from random import randint, randrange
dice_roll = randrange(1,12)
x = int(input("Guess the dice: "))
if x not in range(1,13):
    print("Bad guess, dice numbers are between 1 & 12")
if x > dice_roll:
    print(f'You lost! You picked a greater number. You chose {x} but it was  {dice_roll}')
elif x < dice_roll:
    print(f'You lost! You picked a smaller number. You chose {x} but it was  {dice_roll}')
else:
    print(f'You Win ! Congratulations! You chose {x} and the dice was {dice_roll}')
