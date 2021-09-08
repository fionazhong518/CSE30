"""
File name: simple contact
Created by: Fiona Zhong
Date created: 2021-9-3
"""
import sys, pathlib, sqlite3

#VARIABLES
FILENAME = "contact.db"
FIRSTRUN = True

if(pathlib.Path.cwd()/FILENAME).exists():
    FIRSTRUN = False
CONNECTION = sqlite3.connect(FILENAME)
CURSOR = CONNECTION.cursor()

# ---- FUNCTION --- #

def menu():
    '''
    user's choice
    
    return: CHOICE(int)
    '''
    print('''
    Welcome to Simple Contact!
    1. add a new contact to the list
    2. print all contacts in the list
    3. print where the contact is stored
    4. update the contact on the list
    5. delete a contact in the list
    6. EXIT PROGRAM
    ''')
    CHOICE = input ("Choice: ")
    try:
        choice = int(CHOICE)
        return choice
    except ValueError():
        print("Please put in a valid number")
        return menu()

#INPUT
def addContact():
    """
    add a new name to the contact
    auto save in database file
    """
    global CONNECTION, CURSOR
    #input
    FIRST_NAME = input("First name >")
    LAST_NAME = input("Last name >")
    PHONE_NUM = input("Phone Number(no more than 11 digit) > ")
    EMAIL = input("Email Address > ")
    #processing
    CURSOR.execute('''
        INSERT INFO
            contacts(
                first_name,
                last_name,
                phone_num,
                email
            )
        VALUES(
            ?,?,?,?
        )
    ;''', [FIRST_NAME, LAST_NAME, PHONE_NUM, EMAIL])
    #output
    CONNECTION.commit()
    print("%s %s successfully saved to contacts" % (FIRST_NAME, LAST_NAME))

def searchContact():
    """
    ask user for contact info to search for

    return:
    NAME(str): First name to be search for
    """
    NAME = input("Name: ")
    return NAME


#PROCESSING
def setup():
    """
    create the contacts table if it is the first run
    """
    global CURSOR, CONNECTION

    CURSOR.execute('''
        CREATE TABLE contacts(
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL
            last_name TEXT NOT NULL
            phone_num INTEGER NOT NULL
            email TEXT
        )
    ;''')

    CONNECTION.commit()
    
#OUTPUT


#MAIN PROGRAM CODE
if FIRSTRUN:
    setup()

    While (True):
        CHOICE = menu()
        if CHOICE == 1:
        #add contact
         addContact()
    
        else:
            print("Please enter a valid number!")


