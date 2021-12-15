'''
Name: OOP Character Class Assignment
Author: Fiona Zhong
Date created: 2021-12-15
'''
import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, name, phrase1, phrase2):
        super().__init__()

        self.name = name
        self.phrase1 = phrase1
        self.phrase2 = phrase2
        self.level = 0

    def speak(self, phraseNum):
        if phraseNum == 1:
            print(self.phrase1)
        elif phraseNum == 2:
            print(self.phrase2)

    def setLevel(self, newLevel):
        self.level = newLevel
        print(self.level)

panda = Character('Kung Fu Panda', 'Skadoosh', 'You have been blinded by pure awesomeness!')
spiderman = Character('Spiderman', 'My Spider-Sense is tingling', 'Your friendly neighbourhood sipderman')

panda.speak(1)
spiderman.setLevel(2)
spiderman.speak(2)