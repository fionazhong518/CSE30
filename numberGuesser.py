"""
Name: Number Guessing Game
Author: Fiona ZHong
Date Created: 2021-9-7
"""
import random, sys

# VARIABLES
#Run = True
WIN = False


# INPUT
def getNum():
    
    

    PLAYER = input("> ")
    try:
        PLAYER = int(PLAYER)
        return PLAYER
    except ValueError:
        print("Please enter a valid number.")
        return getNum()

# PROCESSING
def CompareNum(PLAYER, RandomNumber):
    '''
    to see if the user guess the right number, otherwise the program would
    ask the user to guess again

    parameter:
    PLAYER(int): player's choice
    RandomNumber(int): number that the comp picks

    Return:
    DIFF(int): compare PLAYER with RandomNumber, = 0 if the user get it right
    '''
    #global PLAYER, RandomNumber

    DIFF = PLAYER - RandomNumber
    
    if DIFF > 0:
        print("It is too high.")
        return 0
    elif DIFF < 0:
        print("It is too low")
        return 0
    else:
        print("YESSSSS, YOU GOT IT RIGHT! ")
        return 2
    #return DIFF

# START & END SCREEN
def StartScreen():
    '''
    welcome message
    '''
    print("Welcome to Numer Guessing Game!")
    print("I am thinking a number, guess what is it?")

def EndScreen(Winner):
    '''
    ask if the user want to play it again

    parameter:
    END(int): 1 = win, 0 = lost
    '''
    global WIN

    if Winner == 2:
        print("Do you want to play it again? y/N")
        return 1
    elif Winner == 1:
        print('''
Sorry, you are using out of your chance!
Thank you for playing and...
Do you want to play it again? y/N 
        ''')
        return 1
    else:
        pass
        
def playAgain(End):

    global WIN

    if End == 1:
        AGAIN = input("> ")
        if AGAIN != "y" and AGAIN != "Y":
        
            print("Sure, byebye~ ")
            sys.exit()
        else:
            WIN = False

while not WIN:
    
    StartScreen()
    RandomNumber = random.randint(1, 100)
    print(RandomNumber)
    for i in range(5):
        PLAYER = getNum()
        Winner = CompareNum(PLAYER, RandomNumber)
        End = EndScreen(Winner)
        playAgain(End)

    Winner = 1
    End = EndScreen(Winner)
    playAgain(End)
    # having problems with ending the game with users input "y/N"
    # why it just couldn't read my letter :(

while WIN:
    print("you win")
    Winner = 1

    EndScreen()