'''
Name: OOP Backpack Class Assignment
Author: Fiona Zhong
Date created: 2021-12-15
'''
import pygame


class Backpack(pygame.sprite.Sprite):
    def __init__(self, color, size):
        super().__init__()

        self.color = color
        self.size = size
        self.items = []
        self.open = False

    def openBag(self):
        self.open = True
        print(self.color + self.size + ' bag is opened')

    def closeBag(self):
        self.open = False
        print(self.color + self.size + ' bag is closed')
    
    def putin(self,item):
        if self.open:
            self.items.append(item)
            print('Successfully put ' + item + ' into the bag')
    
    def takeout(self,item):
        for i in self.items:
            if self.open and item == i:
                self.items.remove(i)
                print('Successfully took out ' + item)
            

bag1 = Backpack('blue ', 'small')
bag2 = Backpack('red ', 'medium')
bag3 = Backpack('green ', 'large')

bag2.openBag()
bag2.putin('lunch')
bag2.putin('jacket')
bag2.closeBag()
bag2.openBag()
bag2.takeout('jacket')
bag2.closeBag()