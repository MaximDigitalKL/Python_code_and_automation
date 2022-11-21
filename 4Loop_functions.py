'''1. Given the list:
cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
use for to iterate through the list and do the following:
● ‘My favorite car is x’.
● do the same using for each
● do the same using while.'''


cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for i in range(0,len(cars)):
    print(f'My favorite car is: {cars[i]}')
print ("-------------------------------------------------------")
for car in cars:
    print(f'My favorite car is: {car}')
print ("-------------------------------------------------------")
i = 0
while i < len(cars):
    print(f'My favorite car is: {cars[i]}')
    i += 1

'''2. Same list:
user for - else 
in for:
- modify the elements in the list, all should be capitalized except the first and the last
in else:
- print the list .'''
print('--------------------------------------------------')
for i in range(1, len(cars) - 1):
    cars[i] = cars[i].upper()
else:
    print(cars)

'''3. Same list:
There is a buyer who wants to buy a Mercedes
Iterate through the list:
- if the car is "mercedes" print: we found the car you are looking for
- leave the cycle.
Else:
print: we could not find car x, we will keep looking'''

desire = input(f'Choose a car: ')
for i in range(len(cars)):
    if cars[i] == desire:
        print(f'We found the car you are looking for')
        break
    else:
        print(f'We could not find car {desire}. We will keep looking')

'''4. Same list:
We have a buyer that is undecided
- we will present all the cars except "Trabant" and "Lastun"
- If the car is "Trabant" or "Lastun
    use a key word to skip and move to the next one
-print: You might like car x
'''
for i in range(len(cars)):
    if (cars[i] == "TRABANT") or (cars[i] == "LASTUN"):
        continue
    print(f'You might like car: {cars[i]}')

'''5. Modernize your car list:
- Create an empty list old_models
- iterate through the list cars
- when you find Trabant or Lastun - move them to the old_models list
- overwrite them with Tesla in the cars list
- print both lists'''

old_models = []
for i in range(len(cars)):
    if (cars[i] == "TRABANT") or (cars[i] == "LASTUN"):
        old_models.append(cars[i])
        cars[i] = "Tesla"
print(f'Old models {old_models}')
print(f'New models {cars}')

'''6. You have dictionary:
car_prices = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000 }
There is a client with a budget of 15000 euro.
- print only the cars within his budget
      - go through the dictionary and print the car and the price
      - print: For a budget of 15000 euro you can choose car x'''

car_prices = {
'Dacia': 6800,
'Lastun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
for key in car_prices:
    if car_prices.get(key) < 15000:
        print(f'For a budget of 15000 euro you can choose car: {key} at the price of {car_prices[key]} EUR')

'''7. You have the following list:b
numbers = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
- Iterate through the list and print how many times you have the value 3 (can not use count)'''
numbers = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
i = 0
j = 0
while i < len(numbers):
    if numbers[i] == 3:
        j += 1
    i += 1
print(f'Number 3 appears {j} times')

'''8. Same list:
- Iterate through the list and calculate the sum of all the elements (can not use sum function)'''
i = 0
sum = 0
while i < len(numbers):
    sum += numbers[i]
    i += 1
print(f'Sum of the elements is: {sum}')

'''9. Same list:
- Iterate through the list, print the largest number (can not use max function)'''
i = 0
max = 0
for i in range(len(numbers)):
    if numbers[i] > max:
        max = numbers[i]
print(f'The largest number is: {max}')

'''10. Same list:
- Iterate through the list, if the number is positive replace it with it's negative value
- print the new list '''
i = 0
negative = []
for i in range(len(numbers)):
    if numbers[i] > 0:
        negative.append(numbers[i] * -1)
    else:
        negative.append(numbers[i])
print(negative)

'''11. new_numbers = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
positive_numbers = []
negative_numbers = []
even_numbers = []
odd_numbers = []
Iterate through new_numbers, populate all the lists and print them '''
new_numbers = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
even_numbers = []
odd_numbers = []
positive_numbers = []
negative_numbers = []
i = 0
for i in range (len(new_numbers)):
    if new_numbers[i] < 0:
        negative_numbers.append(new_numbers[i])
    else:
        positive_numbers.append(new_numbers[i])
    if new_numbers[i] % 2 == 0:
        even_numbers.append(new_numbers[i])
    else:
        odd_numbers.append(new_numbers[i])
print(f'Positive numbers list: {positive_numbers}')
print(f'Negative numbers list: {negative_numbers}')
print(f'Odd numbers list: {odd_numbers}')
print(f'Even numbers list: {even_numbers}')

'''2. Same list:
- sort the list ascending without using the sort function
'''
y = 0
i = 0
no = 0
while y < len(new_numbers):
    for i in range((len(new_numbers) - 1)):
        if new_numbers[i] > new_numbers[i + 1]:
            no = new_numbers[i]
            new_numbers[i] = new_numbers[i + 1]
            new_numbers[i + 1] = no
    y += 1
print(new_numbers)

'''3. Guess the number:
secret number = generate a random number between 1 and 30
guess_the_number = None
User picks a number, he has 3 chances
The machine answers:
* secret_number is greater
* secret_number is lower
* Congratulations, you guessed right !'''
from random import randint, randrange
secret_number = randrange(1, 30)
guessed_number = 0
chances = 3
while chances > 0:
    guessed_number = int(input(f'Guess the number: '))
    if guessed_number > secret_number:
        print(f'Secret number is smaller')
    elif guessed_number < secret_number:
        print(f'Secret number is greater')
    else:
        print(f'Congratulations, you guessed right !')
    chances -= 1
print(f'You have exhausted all your chances')

'''4. Enter a number from keyboard
Eg: 7
Write a code that will generate the below pyramid
1
22
333
4444
55555
666666
7777777
Eg:3
1
22
333'''
pyramid = int(input('Pick a number from 2 to 9: '))
for i in range(1, pyramid + 1):
    print(str(i)*i)

'''5. Phone keypad = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
Iterate through the list 2d
print ‘The current number is x’
'''
phone_keypad = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
i = 0
j = 0
for i in range(len(phone_keypad)):
    for j in range(len(phone_keypad[i])):
        print(f'The current number is: {phone_keypad[i][j]}')

'''6. Guess the dice using While, user has 3 chances
counter: guessed - false
first iteration :
if number is correct: You guessed right! Congratulations!  guessed = true
if number is lower: You chose a lower number, you have 2 more chances
if number is greater: You chose a greater number, you have 2 more chances
second iteration:
if number is correct: You guessed right! Congratulations!  guessed = true
if number is lower: You chose a lower number, you have 1 more chance
if number is greater: You chose a greater number, you have 1 more chance
third iteration:
if number is correct: You guessed right! Congratulations!
  At the end we evalute the counter 
  if true: The game is over, you won !
  if false: The game is over, you lost !
'''
from random import randint, randrange
dice_roll = randrange(1,12)
tries = 3
guessed=False
while tries > 0:
    x = int(input("Take a guess: "))
    if tries != 1:
        if x == dice_roll:
            print("You guessed right! Congratulations!")
            guessed = True
            break
        elif x < dice_roll:
                print(f'You chose a lower number, you have {tries-1} more chances')
        else:
             print(f'You chose a greater number, you have {tries-1} more chances ')
    else:
        if x == dice_roll:
            print("You guessed right! Congratulations!" )
            guessed = True
            break
        elif x < dice_roll:
                print('You lost ! you chose a lower number')
        else:
             print('You lost ! you chose a greater number')
    tries -= 1
if guessed:
    print('The game is over, you won !')
else:
    print(f'The game is over, you lost !')
