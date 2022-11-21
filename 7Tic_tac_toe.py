from tabulate import tabulate


def player1():
    p1 = input("Player one choose row and column: ")
    row = int(p1[0]) - 1
    column = int(p1[1]) - 1
    i = 0
    j = 0
    for i in range(3):
        if i == row:
            for j in range(3):
                if j == column:
                    table[i][j] = "X"
    print(*table, sep="\n")
def player2():
    p1 = input("Player two choose row and column: ")
    row = int(p1[0]) - 1
    column = int(p1[1]) - 1
    i = 0
    j = 0
    for i in range(3):
        if i == row:
            for j in range(3):
                if j == column:
                    table[i][j] = "0"
    print(*table, sep="\n")

def check():
    win = False
    if table[0][0] == table[0][1] == table[0][2] or table[1][0] == table[1][1] == table[1][2] or table[2][0] == \
            table[2][1] == table[2][2]:
        win = True
    if table[0][0] == table[1][0] == table[2][0] or table[0][1] == table[1][1] == table[2][1] or table[0][2] == \
            table[1][2] == table[2][2]:
        win = True
    if table[0][0] == table[1][1] == table[2][2] or table[0][2] == table[1][1] == table[2][0]:
        win = True
    return win

table = [["R1c1", "R1c2", "R1c3 "], ["R2c1", "R2c2", "R2c3"], ["R3c1", "R3c2", "R3c3"]]
print(tabulate(table))
i = 1
while i <= 4:
    win = False
    player1()
    check()
    if check():
        print("Player 1 (X)  WINS !!!")
        break
    player2()
    check()
    if check():
        print("Player 2 (0)  WINS !!!")
        break
    i += 1
if check() == False:
    print("Game ended in a draw")


