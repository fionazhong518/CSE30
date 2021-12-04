'''
name: 
'''
import pygame

# field or attributes for defining
class Character(): 
    name = "Link"
    sex = "Male"
    max_hit_points = 50
    current_hit_points = 50
    max_speed = 10
    armor_amount = 8


class Dog():
    # ------ CLASS ATTRIBUTES ------ #
    #age = 0
    name = ""
    #weight = 0

    # ------  CLASS METHODS TO DO ATTRIBUTES------ #
    #             (What attributs can do)

# Define FUNCTION INSIDE the CLASS so that it can read the class info
    '''
    def bark(self): #here self will match with my_dog
        print(self.name, " says Bark")

    def poop(self): # ALL NEED TO HAVE self as parameters
        self.weight -= 0.25 # when DOG done Pooping, it will lose 0.25 of its weight
    '''
    #       NOTE: here | name is a local variable to init function
    def __init__(self,name): ### Constructor of Dog()
        #    Caution: You CANNOT call my_name as name like above cuz it will overwrite with " "
        #             Unless you use name too below "self_name = name"
        print("A new dog has born!")
        self.name = name # NOTE: here name is a class variable
        # my_name = self -> my_dog = Dog("Spot")

my_dog = Dog("Spot") #"Spot" = my_name as the second parameter in __init__

print("The dog's name is: ", my_dog.name)

'''
my_dog.weight = 10
my_dog.name = "Spot"
my_dog.bark() # Usually 1 vari in def, 1 vari in defining ()

my_dog2 = Dog()
my_dog2.weight = 5
my_dog2.name = "Fluffy"
my_dog2.bark()

my_dog.poop()
my_dog2.poop()

print(my_dog.weight)
print(my_dog2.weight)
'''

def display_character(my_character):
    print(my_character.name,
    my_character.sex,
    my_character.max_hit_points,
    my_character.current_hit_points,
    my_character.armor_amount)

#creates an instance of the class(object)
# |variable that points the specific obj
## Dot Operator - pull out individual field/attribute to define a particular obj
my_dude = Character() #() necessary
my_dude.name = "Sally"
my_dude.sex = "Female"
my_dude.max_hit_points = 60

his_dude = Character()
his_dude.name = "Bob"


display_character(my_dude) # prints all the fields of my_dude
display_character(his_dude)

class Person:
    name = ""
    money = 0

bob = Person()
bob.name = "Bob"
bob.money = 100

nancy = Person()
nancy.name = "Nancy"
nancy.money = bob.money

print(bob.name, "has", bob.money, "dollars." )
print(nancy.name, "has", nancy.money, "dollars.")

# --------- Inheritance Example --------- #
'''
You can use "[child class] is a [parent class]" sentence to test if the inheritance is proper
in this case: Submarine is a Boat (ok)
            Boat is a Submarine (nonono)
Also, we can use a class diagram that [child class]s is pointed to the [parent class] with a empty arrow
'''
class Boat(): # Parent class --> generalize
    tonnage = 0
    name = ""
    isDocked = True
 
    def dock(self):
        if self.is_docked:
            print("You are already docked.")
        else:
            self.is_docked = True
            print("Docking")
 
    def undock(self):
        if not self.is_docked:
            print("You aren't docked.")
        else:
            self.is_docked = False
            print("Undocking")

# NOTE: things in Boat class would be copyed to Submarine
    #Why to do this? Add a new function that work in all classes but want to to be in the new class
    # Avoid recreating a new but similar class 
    # So like Submarine can do the same things as Boat(), but it can do more (you dont meed to copy paste anymore)

# if change in boat class, also change in Submarine class
class Submarine(Boat): # Child Class --> more specific
    def submerge(self):
        print("Submerge!")

## ANOTHER METHOD: Use super().  to call the parent class
'''
class Spaceship(Boat):
    def __init__(self):
        # call the parent/super class constructor first
        super().__init__()

        # now set up child class variables
        self.ship_title = ""

enterprise2.ship_title = "Sunset"
enterprise3.ship_title = "Sunrise"
'''

enterprise2 = Boat()
enterprise2.name = "Enterprise II"
enterprise2.tonnage = 25

enterprise3 = Boat()
enterprise3.name = "Enterprise III"
enterprise3.tonnage = 100