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
    except ValueError:
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
        INSERT INTO
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


#PROCESSING
def setup():
    """
    create the contacts table if it is the first run
    """
    global CURSOR, CONNECTION

    CURSOR.execute('''
        CREATE TABLE contacts(
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone_num INTEGER NOT NULL,
            email TEXT
        )
    ;''')

    CONNECTION.commit()

def quaryContact():
    '''
    quary the contact that user want
    parameter:
    search_name: name to search

    return:
    search_array: list of the quaried contact info
    '''
    global CURSOR

    search_name = input("What is the first name? ")
    search_array = CURSOR.execute('''
        SELECT
            first_name,
            last_name,
            phone_num,
            email
        FROM
            contacts
        WHERE
            first_name = ?
        ORDER BY
            last_name
        ;''',[search_name]).fetchall()
    
    for i in range(len(search_array)):
        print(search_array[i])

def getID():
    '''
    give every contacts an id for user to choose to edit
    
    return:
    ID: indicate the contact to edit
    '''
    global CURSOR
    CONTACTS = CURSOR.execute('''
        SELECT
            id,
            first_name,
            last_name
        FROM
            contacts
    ;''').fetchall()

    print("Please select a contact: ")
    for i in range(len(CONTACTS)):
        print("%s. %s %s" % CONTACTS[i])

    ID = input("Which one to choose(enter id index)> ")
    # check if the user enter a digit
    try:
        ID = int(ID)
        return ID
    except ValueError:
        print("Please enter a integer!")
        return getID()

    
def updateContact(ID):
    '''
    update a contact in the file
    parameter:
    name: first name of the contact to update
    new_first: new first name
    new_last: new last name
    new_phone: new phone number
    new_email: new email
    '''
    global CURSOR, CONNECTION
    
    old_contact = CURSOR.execute('''
        SELECT
            first_name,
            last_name,
            phone_num,
            email
        FROM
            contacts
        WHERE
            id = ?
    ;''',[ID]).fetchone()
    print("Old contact - ",old_contact)

    new_first = input("New first name: ")
    new_last = input("New last name: ")
    new_phone = input("New phone number: ")
    new_email = input("New email: ")
    new_info = [new_first,new_last,new_phone,new_email, ID]
    CURSOR.execute('''
        UPDATE
            contacts
        SET
            first_name = ?,
            last_name = ?,
            phone_num = ?,
            email = ?
        WHERE
            id = ?
        ;''',new_info) #NOTE: new_info has 5 variable, so the first-four go to SET, and last one go to WHERE
    CONNECTION.commit()

def deleteContact(ID):
    '''
    delete a contact from the list
    parameter:
    ID: ID index of the contact to delete
    '''
    global CURSOR, CONNECTION
    
    CURSOR.execute('''
        DELETE FROM
            contacts
        WHERE
            id = ?
    ;''',[ID])
    CONNECTION.commit()

#OUTPUT
def displayAll():
    '''
    display all the contacts in the file
    '''
    global CURSOR
    CONTACT = CURSOR.execute('''
        SELECT
            first_name,
            last_name,
            phone_num,
            email
        FROM
            contacts
        ORDER BY 
            first_name
    ;''').fetchall()
    for i in range(len(CONTACT)):
        print("%s %s %s %s" % CONTACT[i])
    

#MAIN PROGRAM CODE
if FIRSTRUN:
    setup()

while True:
    CHOICE = menu()
    if CHOICE == 1:
    #add contact
        addContact()
    elif CHOICE == 2:
        displayAll()
    elif CHOICE == 3:
        quaryContact()
    elif CHOICE == 4:
        ID = getID()
        updateContact(ID)
    elif CHOICE == 5:
        ID = getID()
        deleteContact(ID)
    elif CHOICE == 6:
        print("Thank you for using")
        sys.exit()
    else:
        print("Please enter a valid number!")


