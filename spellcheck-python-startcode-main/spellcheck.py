# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time, sys


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
    #print(dictionary[0:50])
    #print(aliceWords[0:50])
    return dictionary, aliceWords
# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()

def menu():
    print('''
1: Spell Check a Word (Linear Search)
2: Spell Check a Word (Binary Search)
3: Spell Check Alice In Wonderland (Linear Search)
4: Spell Check Alice In Wonderland (Binary Search)
5: Exit
    ''')
    choice = int(input("Enter menu selection (1-5): "))

    return choice
def get_word():
    word = input("Please enter a word: ")
    word.lower()
    return word

# ------ DICTIONARY ----- #
def linearSearch_dic(dictionary,word):
    for i in range(len(dictionary)):
        if word == dictionary[i]:
            return i
    return -1

def binarySearch_dic(dictionary, word):
    low_index = 0
    high_index = len(dictionary)-1
    
    while low_index <= high_index:
        mid_index = int((low_index + high_index)/2)

        if dictionary[mid_index] < word:
            low_index = mid_index + 1
        elif dictionary[mid_index] > word:
            high_index = mid_index - 1
        else:
            return mid_index
    
    return -1
def check_found_dic(word, result):
    elapse_time = end_time - start_time
    
    if result == -1:
        print("%s is NOT IN the dictionary. (%s) seconds" % (word, elapse_time))
    else:
        print("%s is  INT the dictionary at position %s. (%s) seconds" % (word, result, elapse_time))



# ------- Alice Wonderland ------- #
def linearSearch_alice(dictionary, aliceWords):
    num_error = 0
    #for i in range(len(dictionary)):
    for i in range(len(aliceWords)):
        word = aliceWords[i].lower()
        index = linearSearch(dictionary, word)
        if index == -1:
            num_error += 1
    return num_error

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

def binarySearch_alice(dictionary, aliceWords):
    num_error = 0

    for i in range(len(aliceWords)):
        word = aliceWords[i].lower()
        index = binearSearch(dictionary, word)
        if index == -1:
            num_error += 1
    return num_error

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

def check_found_alice(num_error):
    elapse_time = end_time - start_time
    print("Number of words not found in dictionary:", num_error , elapse_time, "seconds")

# Call main() to begin program

while True:
    dictionary, aliceWords = main()
    choice = menu()
    
    if choice == 1:
        start_time = time.time()
        word = get_word()
        result = linearSearch_dic(dictionary, word)
        end_time = time.time()
        check_found_dic(word, result)
    elif choice == 2:
        start_time = time.time()
        word = get_word()
        result = binarySearch_dic(dictionary, word)
        end_time = time.time()
        check_found_dic(word, result)
    elif choice == 3:
        start_time = time.time()
        num_error = linearSearch_alice(dictionary, aliceWords)
        end_time = time.time()
        check_found_alice(num_error)
    elif choice == 4:
        start_time = time.time()
        result = binarySearch_alice(dictionary, aliceWords)
        end_time = time.time()
        check_found_alice(result)
    else:
        sys.exit()  