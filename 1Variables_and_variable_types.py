#1. In your own words, what is a variable ?
#---------a variable is like a box, where we store values of multiple types for a future use------------


#2. Declare are initialize a variable for each of the following types:  string, int, float, bool.

name = 'Maxim'
months = 12
km = 39.66
sign_of_life = True

#3. Use "type" function to see if they are of the desired type

print(type(name))
print(type(months))
print(type(km))
print(type(sign_of_life))

#4. Round the float type variable and overwrite the exisiting value, and check it's type again
km = round(km)
print(type(km))

#5. Print in the console a sentence for each variable

print(f'My name is  {name}')
print(f'The year has {months} months')
print(f'The cruising speed is {km} km/h')
print(f"Schrodinger's cat alive? {sign_of_life}")

#6. Read from keyboard "first name" and "last name", print in console the total length of the name

first_name = 'eduard'
last_name = 'maxim'
print(len(first_name) + len(last_name))

#7. Read from keyboard length and width. Prin in console the area of the Right Angle
w = int(input(f'Enter width: '))
L = int(input(f'Enter length: '))
print(f'The area of the Right Angle is  {w * L} cm')

#8. Given the following string: "Coral is either the stupidest animal or the smartest rock".
      #How many times the word "the" appers in it ?

phrase = "Coral is either the stupidest animal or the smartest rock"
print(f'The group of letters "the" appears  {phrase.count("the", 0, len(phrase))} times')


#9. Same string, replace "the" with "THE".

phrase = "Coral is either the stupidest animal or the smartest rock"
print(phrase.replace("the", "THE", len(phrase)))


#10. Read from keyboard a string made up of an odd number of characters. Print the middel character.

word = input(f'Enter a word: ')
print(word[int(len(word)/2)])

#11. Using asset check if a string is a palindrom
pali = "123454321"
assert pali == (pali[::-1]), "It is not a palindrom"

#12. Using one line of code, read a string from keyboard. Save each word in a variable, print both variables.
sentence= input(f'Enter String: '); first_word, second_word = sentence.split(" "); print(f'{first_word} + {second_word} = {sentence}')


#13. Read a string from keyboard
#      -save the first character in a variable
#      -capitalize the first character in the entrire string, except the first and the last characters:
introduced_word = input(f'Enter your string: ') # "bambolina bubulinab"  "alabala portocala"
fst_letter = introduced_word[0]
segmentation = introduced_word[1:-1]
segmentation = segmentation.replace(fst_letter,fst_letter.upper(),len(segmentation))
print(introduced_word[0] + segmentation + introduced_word[-1])


#14. Read a user and a password from keyboard
#        - print in console: "Password for user x is ****** and it has x characters
#        - ***** will be dynamically calculated regardless of the passwords length

user = input("Insert user: ")
password = input("Insert password: ")
print(f'Password for user {user} is {"*" * len(password)} and it has {len(password)} characters')

#15. Using the assert function check if the phrase "Coral is either the stupidest animal or the smartest rock"
           #is made up of numbers
phrase = "Coral is either the stupidest animal or the smartest rock"
assert phrase.isnumeric() == True, "Error, phrase is not numeric"