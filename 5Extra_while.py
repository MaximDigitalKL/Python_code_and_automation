'''Write a while loop that adds all the numbers up to 100 (inclusive).'''
i=0
sum = 0
while i< 100:
    sum += i
    i += 1
print(sum)

'''Using while loop, if statement and str() function; iterate through the list and if there is a 100.
Print it with its index number. i.e.: "There is a 100 at index no: 5"'''
list = [10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
i = 0
while i < (len(list)):
    if list[i] == 100:
        print(f'There is a 100 at index no: {list.index(list[i])}')
    i += 1

'''Using while loop and an if statement, write a function named name_adder which appends
all the elements in a list to a new list unless the element is an empty string: "".'''
#lst1=["Joe", "Sarah", "Mike", "Jess", "", "Matt", "", "Greg"]
def name_adder():
    list1 = ["Joe", "Sarah", "Mike", "Jess", "", "Matt", "", "Greg"]
    list2 = []
    i = 0
    while i < len(list1):
        if len(list1[i]) != 0:
            list2.append(list1[i])
        i += 1
    print(list2)
name_adder()

'''This time inside a function named name_adder, write a while loop that stops 
appending items to the new list as soon as it encounters an empty string: "".
And prints "There is an empty string and returns the new list."'''
#lst1=["Sam", "", "Ben", "Olivia", "Alicia"]
def name_adder2():
    list1 = ["Sam", "", "Ben", "Olivia", "Alicia"]
    list2 = []
    i = 0
    while i < len(list1):
        if len(list1[i]) != 0:
            list2.append(list1[i])
        else:
            print('There is an empty string')
            break
        i += 1
    print(f'The new list is: {list2}')
name_adder2()