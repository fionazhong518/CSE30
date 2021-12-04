"""
Name: Simple Contact (List version)
Author: Fiona Zhong
Date created: 2021-09-10
Date finished: 2021-9-17
"""
import sys

# ---- VARIABLES --- #
NAMELIST = []
RUN = True


# --- INPUT --- #
def addName():
    '''
    ask user what name to add to the list
    updated version : user can add email, phone# to the list under each names

    return:
    NAMELIST(list): list with new name added
    '''
    global NAMELIST

    
    NAME = input("What name would you like to add? >>> ")

    PHONE = input("What is this person's cell number? >>> ")

    EMAIL = input("What is this person's email? >>> ")

    NAMELIST.append([NAME, PHONE, EMAIL])    

    return NAMELIST

# --- PROCESSING --- #
def updateName():
    '''
    update a name in the list

    parameter:
    NAMELIST(list): all name in the list
    
    return:
    NAMELIST(list): list with updated name
    '''
    global NAMELIST

    for i in range(len(NAMELIST)):
        print(NAMELIST[i])

    OLD_INFO = int(input('''
which contact would you like to update? 
enter the index # (starts from 1)
>>> '''))
    OLD_INFO = OLD_INFO - 1

    print("what would you like input instead? >>> ")
    NEW_NAME = input("New Name: ")
    NEW_PHONE = input("New Phone #: ")
    NEW_EMAIL = input("New Email: ")
        
    NAMELIST[OLD_INFO][0] = NEW_NAME
    NAMELIST[OLD_INFO][1] = NEW_PHONE
    NAMELIST[OLD_INFO][2] = NEW_EMAIL

    print("New name has successfully updated! ")

    return NAMELIST

def deleteName():
    '''
    delete a name in the list

    parameter:
    NAMELIST(list): list with all current names

    return:
    NAMELIST(list): list with name deleted

    '''
    global NAMELIST
# ALWAYSSSSSS call for loop in any function

    for i in range(len(NAMELIST)):
        print(NAMELIST[i])

    DELETE_INDEX = int(input("""
Which contact do you want to delete? 
Enter its index number 
Starts from 1 >>> """))
    DELETE_INDEX = DELETE_INDEX - 1

    '''
    for i in range(len(NAMELIST)):
        if NAMEDELETE == NAMELIST[i]:
            NAMETAKEN = str(NAMELIST[NAMEDELETE].pop(0))
            NAMELIST.remove(NAMEDELETE)
            print("Successfully delete " + NAMETAKEN + "from the contact! ")
        
        else :
            print("Under the index you entered there is no contact!")
            return deleteName()
    '''   
    LENGTH = len(NAMELIST) - 1 # to check if the entered index is out of range
    if DELETE_INDEX > LENGTH:
        print("The index you entered has no contact!")
        return deleteName()
    else:
        NAMETAKEN = str(NAMELIST[DELETE_INDEX][0]) # for printing the finished message

        TRASH = NAMELIST.pop(DELETE_INDEX)

        print("Successfully delete " + NAMETAKEN + "from the contact! ")

        
    return NAMELIST

# --- OUTPUT --- #
def menu():

    print('''
    Welcome to your simple contact (List version)

    1. add a new name to the list
    2. show all contacts in the list
    3. update a current name on the list 
    4. delete a name in the list
    5. EXIT
    ''')
    CHOICE = input("> ")
    try:
        CHOICE = int(CHOICE)
        return CHOICE
    except ValueError:
        print("Please enter a valid number!")
        return menu()

def printAll():
    ''''
    print all name in the list

    parameter:
    NAMELIST(list): all names in the list
    '''
    global NAMELIST
    
    for i in range(len(NAMELIST)):
        print("Name: " + NAMELIST[i][0])
        print("Phone #: " + NAMELIST[i][1])
        print("Email: " + NAMELIST[i][2])
        print("\n")
'''    
    CONTINUE = input("Do you want to continue? y/N > ")
    if CONTINUE == "n" or "N":
        print("Thank you for using Simple Contact!")
        sys.exit()
    else:
        RUN = True
'''
# MAIN PROGRAM CODE #

while RUN:
    CHOICE = menu()
    
    if CHOICE == 1:
        NAMELIST = addName()
        print(NAMELIST)
        #later add index to the list together (2D array)
        #later add more info inside the list (email, cell#)

    elif CHOICE == 2:
        printAll()

    elif CHOICE == 3:
        NAMELIST = updateName()

    elif CHOICE == 4:
        NAMELIST = deleteName()
    elif CHOICE == 5:
        print("Thank you for using the Simple Contact.")
        sys.exit()