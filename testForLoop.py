"""
this is a file to test the for loop function
"""

aList = []
SIZE = 5

#ENTER_1 = input("> ")
#ENTER_2 = input(">> ")

for row in range(SIZE):
    aList.append([])
    for col in range(SIZE):
        aList[row].append((row+1) - col)

print(aList)

