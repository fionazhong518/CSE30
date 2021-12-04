'''
name: 7 basic exercises
author: Fiona Zhong
date created: 2021-09-29
'''
import random


def fahrToCelsius(fahrTemp):
    '''
    user input temperature in Fahr unit, the program converts it to Celsius
    formula: (32F - 32) x 5/9 = 0C

    parameter:
    fahrTemp(int): a fahrenheit temperature
    return:
    cels(int): converted temperature in Celsius
    '''
    
    # processing
    return int((fahrTemp - 32) * 5/9)

#fahrToCelsius(32) 
# randomly input a # so that the function would work, but you can change its value as you want

def analyzeNumber(aNumber):
    '''
    determines if a given number is positive, negative, or zero

    parameter:
    aNumber(int): a number to analyze

    return:
    result(str): indicates whether the given number is positive, negative, or zero
    '''
    
    if aNumber > 0:
        result = str("positive")
    elif aNumber < 0:
        result = str("negative")
    else:
        result = str("zero")

    return result
#analyzeNumber(10)
# randomly input a # so that the function would work, but you can change its value as you want

def countItems(aList, anItem):
    '''
    counts the number of occurrences of the given item in the provided list
    
    parameters:
    anItem(obj): a value to count
    aList(list): a list to search

    return:
    a # indicating the number of times the given item appears
    '''
    ## TWO METHOD HERE
    # --- First Method --- #
    #return aList.count(anItem)

    # --- Second method --- #
    n = 0
    for item in aList:
        if anItem == item:
            n += 1
    return n
# -- first method -- #
#print(countItems(['a','b','c',],'b'))

# -- second method -- #
#n = countItems(['a','a','b','b','x','a'], 'a')
#print(n)

def analyzeList(aList):
    '''
    Print out information about the given list/array.
    1. length of the given list
    2. value of the first element in the given list
    3. value of the last element in the given list
    
    parameter:
    aList(list): a list to analyze
    '''
    
    length = int(len(aList))
    first_element = aList[0]
    last_element = aList[-1]

    print('''
    - Length: {0}
    - First Element: {1}
    - Last Element: {2}
    '''.format(length, first_element, last_element))

#analyzeList(['a','a','b','x','c','d'])

def replaceAll(oldVal,newVal,aList):
    '''
    Modifies the given list/array so that 
    all elements in the array that have the given old value will get replaced with the given new value.
    
    parameters:
    oldVal (?): the value to replace
    newVal (?): the new value to replace the old values with
    aList (list/array): a list/array to modify
    '''
    
    for n,obj in enumerate(aList):
        if obj == oldVal:
            aList[n] = newVal
        else:
            pass
    print(aList,"\n")
#replaceAll('a',5,[1,2,5,1,'a',2,1])

def swap(index1,index2,aList):
    '''
    Modifies the given list/array so that the elements at the two provided index values are swapped

    parameters:
    index1 (Number): the first index/position
    index2 (Number): the second index/position
    aList (list/array): a list/array to modify
    '''
    for i in range(len(aList)):
        if i == index1:
            obj1 = aList[index1]
            obj2 = aList[index2]

            aList[index2] = obj1
            aList[index1] = obj2
    print(aList,"\n")
aList = ['a','b','c','d']
#swap(0,2,aList)



def createRandomList(n,low,high):
    '''
    Creates a list/array with a given number of random values. 
    Random values will be between the provided low (inclusive) and high (exclusive) values.

    parameter:
    n (Number): the number of elements that the array should have
    low (Number): the inclusive low value for the random elements
    high (list/array): the inclusive high value for the random elements

    return:
    my_list(list): list with n element
    Each element should be a random value between the given low (inclusive) and the given high (exclusive).
    '''
    
    
    for i in range(n):
        my_list.append(random.randint(low, high-1))
    print(my_list)

    return my_list
my_list = []
my_list = createRandomList(5,1,5)
"""
# ------- MAIN PROGRAM CODE ----- #
while True:

    #cels = fahrToCelsius()

    #result = analyzeNumber()

    #analyzeList()
    '''
    aList = ['b','a','a','c','a']
    print(aList)
    anItem = input("what value to count? ")

    print(countItems(aList, anItem))
    '''
    #replaceAll()
    #swap()
    my_list = createRandomList()
""" 