'''
Name: Bubble Tea Maker
Author: Fiona Zhong
Date created: 2022-05-15
'''
import random, sys
"""
1. 随机搭配
4. 收钱
5. 正确做奶茶步骤
"""
run = True
# INPUT
BASE = ['milktea', 'milk', 'milkshake', 'yogurt', 'tea']
SUGAR = ['full', 'half', 'no']
ICE = ['full', 'half', 'no', 'hot']
ITEMS = ['brownsugar', 'taro', 'matcha', 'strawberry', 'mango']
ADD_INS = ['coconut jelly', 'red bean', 'tapioca', 'fresh taro', 'purple rice']
"""
def menu():
    print('''
    Welcome!
    1. Brown Sugar Milk Tea  $6.5
    2. Taro Milk Tea         $6.0
    3. Matcha Milk Tea       $6.0
    4. Stawberry Milkshake   $6.5
    5. 

    What can I get for you?
    ''')
    ORDER = input('> ')
    sugar = input('''
    Choose a sugar level:
    1. full sugar
    2. half sugar
    3.no sugar
    input digit >
    ''')
    ice = input('''
    Choose a ice level:
    1. full ice
    2. half ice
    3. no ice
    input digit >
    ''')
    try:
        order = int(ORDER)
        if order == 1:
            order = 'brownsugar milktea'
        elif order == 2:
            order = 'taro milktea'
        elif order == 3:
            order = 'matcha milktea'

        sugar = int(sugar)
        ice = int(ice)
        return order, sugar, ice
    except ValueError:
        print('please input a valid number!')
        return menu()
    
def add_ins():
    print('''
    Any add-ins?
    1. coconut jelly  2. tapioca  3. red bean
    4. fresh taro     5. jelly    6. purple rice
    ''')
    add_in = input('input digit > ')
    try:
        add_in = int(add_in)
        return add_in
    except ValueError:
        print('please input a valid number!')
        return add_ins()
"""
def order():
    '''
    Randomly combine elements to make a drink

    parameter:
    LIST OF SELECTIONS

    return:
    Drink name(list): a random combination of drink
    '''
    x = random.randrange(len(ITEMS))
    item = ITEMS[x]
    LIST = [ITEMS, BASE, ICE, SUGAR, ADD_INS]
    for list in LIST:
        x = random.randrange(len(list))
        if list == ITEMS:
            item = ITEMS[x]
        elif list == BASE:
            base = BASE[x]
        elif list == SUGAR:
            sugar = SUGAR[x]
        elif list == ICE:
            ice = ICE[x]
        elif list == ADD_INS:
            addin = ADD_INS[x]
    
    drink = [item, base, addin, ice]
    print(str('''
    here is your order:
    {0} {1} with {2}, ice/warm: {3} and {4} sugar
    ''').format(item, base, addin, ice, sugar))
    return drink

# PROCESSING
def make_juice():
    '''
    pretend you are making the drink

    parameter:
    drink(list): list of items

    '''
    
    print('''
    黑糖珍珠 | 珍珠 | 芋泥 | 抹茶
    紫米    | 红豆 | 草莓 | 芒果
    ''')
    item = input('加什么主料? > ').lower()
    print('加 '+ item +' 到杯子里')

    print(ADD_INS)
    addin = input('加什么小料(注意空格！) > ').lower()
    print('加 ' + addin + '到杯子里')

    print(ICE)
    ice = input('冰or热饮 > ').lower()
    if ice == 'hot':
        print('拿出纸杯')
    else:
        print('加 '+ ice +'的冰到冰杯里面')

    #choice = None
    
    try:
        choice = int(input('''
        What to do next?
        1. 用破壁机
        2. 加饮料到杯子里
    '''))
        
        if choice == 1:
            print(BASE)
            base = input('加什么到破壁机里？> ')
            print('倒' + base + '进了破壁机')
            print(' 嗡嗡嗡...(搅碎中...)')
            choice = 2
        if choice == 2:
            print("吨吨吨...奶茶倒好封杯！")
    except ValueError:

        print("please enter the valid value")
        return choice


    answer = [item, base, addin, ice]

    return answer
    
def check():
    '''
    check if the user make the right drink
    parameter:
    drink(list): original order
    answer(list): user's answer

    return:
    win(boolean): right/wrong
    '''
    pass



while run:
    #order, suar, ice = menu()
    #tea = make_juice(order)
    drink = order()
    answer = make_juice()
    for things in range(len(drink)):
        if drink[0] == answer[0] and drink[1] == answer[1] and drink[2] == answer[2] and drink[3] == answer[3]:
            win = True
        else:
            win = False
    if win:
        print("you made the right drink!")

    else:
        print("""sorry, you did not make the right drink, 
        please check you order!""")
    again = input('''
    do you want to do the next order?
    y = yes''')
    if again == "y" or again  == "Y":
        run =  True
    else:
        run = False
sys.exit()

