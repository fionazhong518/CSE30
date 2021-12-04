"""
Name: Bubble Sort Function Assignment
Author: Fiona Zhong
Date Created: 2021-11-16
"""



def bubbleSort(anArray):
    '''
    Sort the provided array using the bubble sort algorithm.
    parameter:
    anArray: an array to sort
    '''
    n = len(anArray)
    for i in range(n - 1):
        for j in range(0, n-i-1): 
        #if the last item is on its place, times of comparison -1 to ignore the last item
            if anArray[j] > anArray[j+1]:
                anArray[j], anArray[j+1] = anArray[j+1], anArray[j]
        #print(anArray)          

#anArray = [10, 70, 30, 100, 40, 45, 90, 80, 85]
#anArray = ["dog","at", "good", "eye", "cat", "ball", "fish"]
#bubbleSort(anArray)

def selectionSort(anArray):
    '''
    Sort the provided array using the selection sort algorithm.
    parameter:
    anArray: an array to sort
    '''
    n = len(anArray)
    for i in range(n - 1):
        minpos = i
        # if the value of next index is smaller
        for j in range(i +1, n):
            if anArray[minpos] > anArray[j]:
                minpos = j
        anArray[i], anArray[minpos] = anArray[minpos], anArray[i]
        #print(anArray)
#anArray = [10, 70, 30, 100, 40, 45, 90, 80, 85]
#anArray = ["dog","at", "good", "eye", "cat", "ball", "fish"]
#selectionSort(anArray)

def insertionSort(anArray):
    '''
    Sort the provided array using the insertion sort algorithm.
    parameter:
    anArray: an array to sort
    '''
    n = len(anArray)
    for i in range(1,n):
        inserVal = anArray[i]
        inserPos = i
        while inserPos > 0 and anArray[inserPos-1] > inserVal:
            anArray[inserPos] = anArray[inserPos - 1]
            inserPos = inserPos-1
        anArray[inserPos] = inserVal
        print(anArray)

anArray = [10, 70, 30, 100, 40, 45, 90, 80, 85]
#anArray = ["dog","at", "good", "eye", "cat", "ball", "fish"]
insertionSort(anArray)