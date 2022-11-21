'''1. Declare a list of musical notes
* print the list
* reverse the list using slicing and print it again (reversed)
* use a function that does the exact same thing and reprint the list (it should be like the original list)'''

portable = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
print(portable)
portable = portable[::-1]
print(portable)
portable.reverse()
print(portable)

#2. How many times does "DO" appera in the list
print(f'"DO" appears {portable.count("do")} times')

#3. You have 2 lists, [3, 1, 0, 2] & [6, 5, 4]
              # Print them together using 2 different ways.
l1 = [3,1,0,2]
l2 = [6,5,4]
l3 = l1+l2
print(l3)
for i in range(0,len(l2)):
    l1.append(l2[i])
print(l1)

#4. Sort and print the newly generated list from the previous exercise
              # ● remove number zero form list
              # ● print the list again
l3.sort()
print(l3)
l3.remove(0)
print(l3)

#5. Using if, check if the list is empty or not.
if len(l3) == 0:
    print("List is empty")
else:
    print("List is not empty")

#6. Use a function to clear the list.
l3.clear()
print(l3)

#7. Check again if the list is empty or not.
if len(l3) == 0:
    print("List is empty")
else:
    print("List is not empty")

#8. You have the following dictionary dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
               # use a function to prin the keys
students = {
    "Ana":8,
    "Gigel":10,
    "Dorel":5
}
print(students.keys())

#9. Print the students and their grades:
                # Eg: ‘Ana has taken grade {x}’
                # You will generate only the grade by using keys
print(f'Ana has taken grade {students.get("Ana")}')
print(f'Gigel has taken grade {students.get("Gigel")}')
print(f'Dorel has taken grade {students.get("Dorel")}')


#10. Dorel has complained about the grade and he took a 6
                    # ● Modify his grade to 6
                    # ● Print his grade after the modification
students["Dorel"] = 6
print(f"After complaining Dorel's grade is {students.get('Dorel')}")

#11. Gigel gets transferred
                 # ● use a function to delete Gigel from dictionary
                 # ● add the new student Ionica, with grade 9
                 # ● print the dictionary
students.pop("Gigel")
students["Ionica"] = 9
print(students)

#12. Using a set
                # days_of_the_week = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}
                # weekend = {'Saturday', 'Sunday'}
                # ● add 'Monday' to the set
                # ● Print the set
days_of_the_week = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}
weekend = {'Saturday', 'Sunday'}
days_of_the_week.add('Monday')     #sets do not accept duplicates
print(days_of_the_week)

#13. Check if weekend is a subset of days_of_the_week
if weekend.issubset(days_of_the_week) == True:
    print("Weekend is a subset of days_of_the_week")
else:
    print("Weekend is not a subset of days_of_the_week.")

#14 print the differences between the two sets
print(days_of_the_week.difference(weekend))

#15. Print the intersection between the two sets
print(days_of_the_week.intersection(weekend))

'''1.You have a 5 members football team 
There are 3 changes allowed per match:
   If player x is on the field, you make the change and display how many changes are left.
       -make the change
       -remove the player
       -add the new player
       -print player x has left the field, player y has entered the field, you have y changes left
    If the player is not on the field:
       -print: You can not make the change, player x is not on the field.
       -print: you have y changes left'''

team_fc = ["T.Henry", "C.Ronaldo", "L.Mesi", "A.Iniesta", "M.Salah"]
reserves = ["A.Mutu", "C.Chivu", "G.Hagi"]
print(team_fc)
change = ""
eliminated = ""
number_of_changes_left = 3
while number_of_changes_left <= 3 and number_of_changes_left > 0:
    player = input(f'Choose a player: ')
    if player in team_fc and len(reserves) > 0:
        eliminated = player
        team_fc.remove(player)
        team_fc.append(reserves[0])
        change = reserves[0]
        reserves.remove(reserves[0])
        number_of_changes_left -= 1
        print(f'{change}  entered the field and {eliminated} left, there are {len(reserves)} changes left')
    else:
        print(f'You can not make the change, player {player} is not on the field')
        print(f'There are {len(reserves)} changes left')
print(f'Team at the end of the match is: {team_fc}')

