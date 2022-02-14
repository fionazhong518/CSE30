'''
Name: CCC Practice Problem
Author: Fiona Zhong
Date created: 2022-02-2
'''

# -------- Crazy Fencing
# A = w(h1 + h2)/2

height_list = []
def fencing():
    trapzNum = int(input('')) # first line
    # second line
    print('heights')
    height_list = []
    for i in range(trapzNum + 1):
        height = int(input(''))
        height_list.append(height)
    # third line
    print('widths')
    width_list = []
    for i in range(trapzNum):
        width = int(input(''))
        width_list.append(width)

    # calculation
    area = []
    for i in range(trapzNum):
        w = width_list[i]
        h1 = height_list[i]
        h2 = height_list[i+1]
        a = int(w*(h1+h2)) // 2
        area.append(a)
    Area = sum(area)
    
    print('Numbers of trapezoid', trapzNum)
    print('Heights', height_list)
    print('Widths', width_list)
    print('Total area', Area)


fencing()