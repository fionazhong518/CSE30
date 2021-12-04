'''
Name: Linear/Binary Search Assignment
author: Fiona Zhong
date created: 2021-10-20
'''
def linearSearch(anArray, item):
    '''
    Search the provided array for the provided item using the linear search algorithm.
    
    parameter:
    anArray: an array to search through
    item: an item to look for in the array

    return:
    If the item is found, return the index where found.
    If the item is not found, return -1.
    '''
    for i in range(len(anArray)):
        if item == anArray[i]:
            return i
    else:
        return -1

#print(linearSearch(['a','b','dd','vovo','fafafa'],'vovo'))

def binearSearch(anArray, item):
    '''
    Search the provided array for the provided item using the binary search algorithm.

    parameters:
    anArray: an array to search through (you may assume this array contains sorted data)
    item: an item to look for in the array

    return:
    If the item is found, return the index where found.
    If the item is not found, return -1.
    '''
    low_index = 0
    high_index = len(anArray)-1
    
    while low_index <= high_index:
        mid_index = int((low_index + high_index)/2)

        if anArray[mid_index] < item:
            low_index = mid_index + 1
        elif anArray[mid_index] > item:
            high_index = mid_index - 1
        else:
            return mid_index
    
    return -1

print(binearSearch(['a','boobi','ciaala','d','ooo','walawala'],'ooo'))