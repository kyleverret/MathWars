#start stats

import random
f = open('savr.txt', 'r')
stats = eval(f.read())
f.close()

for name in stats.keys():
    print('Player one is ', name)

HP_max = 5
HP_current = 5
WC = 1
weapon_cur = 'a little stick'
weapon_stash = {'a little stick': 1}
plevel = 1
mlevel = 1
xp = 0
yans = ['Y', 'y', 'yes', 'Yes', 'sure', 'ok', 'yup']
nans = ['N', 'n', 'no', 'No', 'nope', 'negatory']
user_name = ''
username = 'Enter here'

def n_user_name():
    global user_name
    user_name = username.get()
    print(username)

def start_game():
    #name_entry = ttk.Entry(mainframe, width=7, textvariable=username)
    #name_entry.grid(column=2, row=1, sticky=(W, E))

    #ttk.Button(mainframe, text="Start!", command=n_user_name).grid(column=3, row=3, sticky=W)
    #ttk.Label(mainframe, text="Enter your name").grid(column=1, row=1, sticky=W)
    savr = open('savr.txt', 'r')
    print("Welcome to the Land of Mathmatica. What is your name brave Math Warrior?")
    user = str(input("Enter your name:"))
    print('Welcome %s' % user)
    return username


def print_stats():
    print('Your current experience points are %d.' % (xp))
    next_action()

def next_action():
    vstats = ['view', 'v', 'View', 's', 'stats']
    cbat = ['combat', 'c', 'Combat']
    print("What would you like to do:")
    nmove = str(input("View (s)tats  | (C)ombat | (Q)uit"))
    nmove = nmove.lower()
    if nmove in vstats:
        print_stats()
    elif nmove in cbat:
        com_now()
        # play_battle('bob')
        next_action()
    elif 'q' in nmove or 'Q' in nmove:
        print('Goodbye!')
        return
    else:
        print('Invalid move')
        next_action()
    return

def get_answer():
    ans = input("Your answer:")
    try:
        ans = int(ans)
        return int(ans)
    except ValueError:
        print('Invalid move. Please enter a number.')
        get_answer()
        pass

def com_now():
    global xp
    repeater = 1
    while repeater <= 5:
        print('Round', repeater)
        op_type_num = random.randint(1,4)
        if op_type_num == 1:
            op_type = 'plus'
        elif op_type_num == 2:
            op_type = 'minus'
        elif op_type_num == 3:
            op_type = 'times'
        elif op_type_num == 4:
            op_type = 'compare'
        else:
            op_type = 'Error!'
        if op_type_num == 1 or op_type_num == 2:
            num1 = random.randint(0, 100)
            num2 = random.randint(0, 100)
            if op_type == 'plus':
                total1 = num1 + num2
            elif op_type == 'minus':
                if plevel <= 5:
                    highnum = max(num1, num2)
                    lownum = min(num1, num2)
                    num1 = highnum
                    num2 = lownum
                total1 = num1 - num2
            print('It is Battle Time!')
            print(('What is %d %s %d?') % (num1, op_type, num2))
            user_answer = get_answer()
            if user_answer == total1:
                print("Victory!")
                xp += 1
            else:
                print("Incorrect! The correct answer is %d %s %d is %d." % (num1, op_type, num2, total1))
        elif op_type_num == 3:
            num1 = random.randint(0, 10)
            num2 = random.randint(0, 10)
            print('It is Battle Time!')
            total1 = num1 * num2
            print(('What is %d times %d?') % (num1, num2))
            user_answer = get_answer()
            if user_answer == total1:
                print("Victory!")
                xp += 1
            else:
                print("Incorrect! The correct answer is %d times %d is %d." % (num1, num2, total1))
        elif op_type_num == 4:
            comp_type_num = random.randint(1, 2)
            num1 = random.randint(-100, 100)
            num2 = random.randint(-100, 100)
            greater1 = max(num1, num2)
            lesser1 = min(num1, num2)
            print('It is Battle Time!')
            if comp_type_num == 1:
                print('Which is greater: %d or %d?' % (num1, num2))
                user_answer = get_answer()
                if user_answer == greater1:
                    print("Victory!")
                    xp += 1
                else:
                    print("Incorrect! %d is greater than %d." % (greater1, lesser1))
            elif comp_type_num == 2:
                print('Which number is smaller: %d or %d?' % (num1, num2))
                user_answer = get_answer()
                if user_answer == lesser1:
                    print("Victory!")
                    xp += 1
                else:
                    print("Incorrect! %d is less than %d." % (lesser1, greater1))
        else:
            print('Error')
        repeater += 1
    tryagain = str(input('Do you want to battle again?'))
    if tryagain in yans:
        com_now()
    return xp


user_name = start_game()
next_action()
