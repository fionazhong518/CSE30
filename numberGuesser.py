"""
Name: Number Guessing Game
Author: Fiona ZHong
Date Created: 2021-9-7
"""
import random

#Run = True

def PlayerChoice():
    
    PLAYER = input("> ")
    try:
        PLAYER = int(PLAYER)
        return PLAYER
    except ValueError:
        print("Please enter a valid number.")
        return PlayerChoice()

def ComputerChoice():
    RandomNumber = random.randint(1, 100)

    return RandomNumber


while True:
    print("Welcome to Numer Guessing Game!")
    print("I am thinking a number, guess what is it?")

    PLAYER = PlayerChoice()
    #print(PLAYER)
    RandomNumber = ComputerChoice()
    print(RandomNumber)

'''
    if comp == player:
        

    else:
        for i in range(): #(START, END(not included), STEP-go by...)
         print("I am thinking a number, guess what is it?")
'''
