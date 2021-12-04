import random

'''
#we give it a 2 to specify a field width of two characters
# By default, it will try to right-justify numbers and left-justify text.
for i in range(10):
    x = random.randrange(20)
    print("{:2}".format(x) )

''' 
'''
# Even better works with larger integer
# Added commas
for i in range(10):
    x = random.randrange(100000)
    print("{:6,}".format(x) )
'''

# -------- Formatting with a List -------- #
'''
my_fruit = ["Apples", "Oranges", "Grapes", "Pears"]
my_calories = [4, 300, 70, 30]
 
for i in range(4):
    print("{:7} are {:3} calories.".format(my_fruit[i],my_calories[i]) )
    # max # of letter is 7, and max # of digit is 3
    # By default, it will try to right-justify numbers and left-justify text.
'''
# now number is left-justify and text is right-justified
my_fruit = ["Apples", "Oranges", "Grapes", "Pears"]
my_calories = [4, 300, 70, 30]
 
for i in range(4):
    print("{:>7} are {:<3} calories.".format(my_fruit[i],my_calories[i]) )

# ---- Formatting time output ---- #
for hours in range(1,13):
    for minutes in range(0,60):
        print("Time {:02}:{:02}".format(hours, minutes))
        # Rather than specify a 2 for the field width, instead use 02. 
        # This will pad the field with zeros rather than spaces.


# ------- Apllication to Bills ------ #
cost1  = 3.07
tax1   = cost1 * 0.06
total1 = cost1 + tax1
 #If you want to print a floating point number for cost, you use an f
 #     total field width of 5 characters long (including the dot) and 2 decimal allowed (rest will be rounded)
print("Cost:  ${0:5.2f}".format(cost1) ) 
print("Tax:    {0:5.2f}".format(tax1) )
print("------------")
print("Total: ${0:5.2f}".format(total1) )


# NOTE: formatting for the display does not change the number. 
# Use the round command to change the value and truly round.
cost1 = 3.07
tax1 = round(cost1 * 0.06, 2) # It returns the rounded value but does not change the original value.
total1 = cost1 + tax1
 
print("Cost:  ${0:5.2f}".format(cost1) )
print("Tax:    {0:5.2f}".format(tax1) )
print("------------")
print("Total: ${0:5.2f}".format(total1) )
 
cost2 = 5.07
tax2 = round(cost2 * 0.06,2)
total2 = cost2 + tax2
 
print()
print("Cost:  ${0:5.2f}".format(cost2) )
print("Tax:    {0:5.2f}".format(tax2) )
print("------------")
print("Total: ${0:5.2f}".format(total2) )
 
 
print()
grand_total = total1 + total2
print("Grand total: ${0:5.2f}".format(grand_total) )
