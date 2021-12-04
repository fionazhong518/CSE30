'''
Name: Simple Contact (Class version)
Author: Fiona Zhong
Date Created: 2021-09-28
'''
# Gobal variables
contacts = []

# Define Class Atrributes
class infoType():
    
    def _init_ (self):
        self.name = "",
        self.phone = "",
        self.email = ""
    # To decide 
    def __str__(self):
        return self.name + "," + str(self.phone) +"," + str(self.email) 

def askName():
    '''
    get users name and create a new class to store info

    return:
    UserName(str): user name
    '''
    name = str(input("What name to add? > "))

    return name

def getInfo(name):
    '''
    get users information

    parameter:
    Name(str): name to create new class

    return:
    someone.name: name
    someone.phone: his/her phone number
    someone.email: his/her email address
    '''
    # create a contact
    ## NOTE: here x is a local variable, not global!
    ## ERROR: MUST define a local vari to interact with CLASS
    ## instead of straightly use the input name like USERNAME.name = str(USERNAME)
    ## because that would overwrite the USERNAME to a obj, not self
    x = infoType()

    # set the fields in the contact
    ## NOTE: x local vari is defined as user_name = name in main
    x.name = str(name) #have to use a separate vari for defining class, so the input username can be a obj(str)
    x.phone = int(input("What is the phone number? > "))
    x.email = str(input("What is the email address? > "))

    contacts.append(x)
    for contact in contacts:
        print(contact)


while True:
    user_name = askName()
    getInfo(user_name)

