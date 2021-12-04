# SORT ANALYZER STARTER CODE

import time

# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS
def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp


# LOAD DATA FILE INTO GLOBAL VARIABLES
anArray = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")

# VERIFY LOADED DATA BY PRINTING FIRST 50 ELEMENTS
#print(anArray[0:50])
#print(reversedData[0:50])
#print(nearlySortedData[0:50])
print(fewUniqueData[0:150])


# EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
# startTime = time.time()
# bubbleSort(anArray)
# endTime = time.time()
# print(f"Bubble Sort Random Data: {endTime - startTime} seconds")

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
#startTime = time.time()
#bubbleSort(anArray)
#endTime = time.time()
#print(f"Bubble Sort Random Data: {endTime - startTime} seconds")

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
#startTime = time.time()
#selectionSort(fewUniqueData)
#endTime = time.time()
#print(f"Selection Sort Random Data: {endTime - startTime} seconds")


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
startTime = time.time()
insertionSort(fewUniqueData)
endTime = time.time()
print(f"Insertion Sort Random Data: {endTime - startTime} seconds")