'''


'''
import sys

WIN = True
word = ['m', 'a', 'n', 'g', 'o']
answer = ['_','_','_','_','_']

def startScreen():
    '''
    start message
    '''
    print('''
I am thinking about a word,
guess what is it?''')

def getword(answer):
    '''
    get the user's input and compare
    '''
    global word

    chance = 6
    
    guess_letter = input("guess a letter ").lower()
    
    if chance != 0:
        for position in range(len(word)):
            if word[position] == guess_letter:
                answer[position] = guess_letter
            else:
                pass
        chance = chance - 1

        print(answer)
    else:
        print("You are using out of chance!")
    
    return answer

def endScreen():
    '''
    
    '''



while True:
    startScreen()
    getword(answer)
