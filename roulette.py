from pickle import FALSE, TRUE
import random

'''Simulate A Roulette table - Katie
36 numbers in 3 cols of 12 rows
red nums:   1,3,5,7,9,12,14,16,18,21,23,25,27,30,32,34,36

any number
reds/blacks
even/odd
fall within 1-18
fall within 19-36 
specific col
specific row

let user bet and report whether win or loss
continue until user enters quit or has no money
keep track of winnings
allow user to check balance
'''
""" ===============================================
Below are the roll and balance functions. 
Computes the roll on the board
returns result
returns current balance
=============================================== """ 
def roll():
    result = random.randint(0,36)
    #print(result)
    return result


def get_balance():
    global balance
    return balance



""" ===============================================
Below are win/loss functions. 
updates balance based on type of bet made by the user
and whether they won or lost
=============================================== """
def won(num=0, clr=0, eo=0, grp=0, col=0, row=0):
    global balance

    #if the user wins their particular bet, add the appropriate $
    print("You won.")
    if  num == 1:
        balance += 35
    elif clr == 1:
        balance += 1
    elif eo == 1: 
        balance += 1
    elif grp == 1:
        balance += 1
    elif col == 1:
        balance += 2
    elif row == 1:
        balance += 11

def lost():
    global balance

    #else, if the user loses, subtract one from their balance
    print("You lost.")
    balance -= 1



""" ===============================================
Below are the betting functions. 
Handles differently based on type of bet made by the user
and whether they won or lost
=============================================== """
#any_number() allows user to bet any number on the board
def any_number(roll, bet):

    print("\n\nRoll was:", roll)
    
    #if the roll num is equal to the bet num,
    if roll == bet:
        won(num=1) #call won() and set num=1 to win appropriate amount
    else:
        lost()



#red_black() allows user to bet any color on the board
def red_black(roll, bet):

    #set the winnning color
    if roll in red:
        color="red"
    elif roll in black:
        color="black"
    else:
        color="green"

    print("\n\nRoll was: {} which is {}".format(roll, color))

    #if bet is equal to winning color,
    if bet == color:
        won(clr = 1) #call won() and set clr=1 to win appropriate amount
    else: 
        lost()



#even_odd() allows user to bet either even or odd
def even_odd(roll, bet):

    #set winning guess
    if roll in even:
        guess="even"
    elif roll in odd:
        guess="odd"

    print("\n\nRoll was: {} and that is {}".format(roll, guess))

    #if bet is equal to winning guess,
    if  bet == guess:
        won(eo = 1) #call won() and set eo=1 to win appropriate amount
    else: 
        lost()



#grouped_nums() allows user to bet number falls in either group 1 or 2
def grouped_nums(roll, bet):

    #if bet was group 1 (1-18) and the roll falls between 1-18,
    if bet == 1 and 1 <= roll <= 18:
        guess = TRUE
    #or if bet was group 2 (19-36) and the roll falls between 19-36,
    elif bet == 2 and 18 < roll <= 36:
        guess = TRUE
    else: 
        guess = FALSE

    print("Roll was:", roll)

    #if user won their group,
    if guess == TRUE:
        print("That falls in the group!")
        won(grp=1) #call won() and set grp=1 to win appropriate amount
    else:
        print("Doesn't fall in the correct group.")
        lost()



#column_bet() allows user to bet between the three columns
def column_bet(roll, bet):

    #set columns  Note: the first 'column' is the one on the bottom of the board
    col1 = {1,4,7,10,13,16,19,22,25,28,31,34}
    col2 = {2,5,8,11,14,17,20,23,26,29,32,35}
    col3 = {3,6,9,12,15,18,21,24,27,30,33,36}
    
    #determine winning column
    if roll in col1:
        column = 1
        name = "column 1"
    elif roll in col2:
        column = 2
        name = "column 2"
    elif roll in col3:
        column = 3
        name= "column 3"

    print("\n\nRoll was: {} which is in {}".format(roll, name))

    #if bet is equal to winning column,
    if bet == column:
        won(col=1) #call won() and set col=1 to win appropriate amount
    else:
        lost()



#row_bet() allows user to bet between the 12 rows
def row_bet(roll, bet):

    #set rows
    rows = { 
        "row.0" : [0],
        "row.1" : [1,2,3],
        "row.2" : [4,5,6],
        "row.3" : [7,8,9],
        "row.4" : [10,11,12],
        "row.5" : [13,14,15],
        "row.6" : [16,17,18],
        "row.7" : [19,20,21],
        "row.8" : [22,23,24],
        "row.9" : [25,26,27],
        "row.10" : [28,29,30],
        "row.11" : [31,32,33],
        "row.12" : [34,35,36],
    }

    #pull the winning row
    winningRow = ''
    for key,value in rows.items():
        if roll in value:
            winningRow = key

    #format and obtain the integer of the winning row
    winningRow = int(winningRow.split('.')[1])

    print("\n\nRoll was: {} which is in row {}".format(roll, winningRow))

    #if bet equal to the winning row number,
    if bet == winningRow:
        won(row=1) #call won() and set row=1 to win appropriate amount
    else:
        lost()



""" ===============================================
Below are the menus. 
Prints the corresponding menu to user inputs
=============================================== """

'''
make_bet()
gather input, validate input, and call subsequent function to
produce the roll and outcome of the game
'''
def make_bet():
    #print the menu and gather user input
    print_bet_menu()
    bet_op = input("\nWhat bet would you like to place? ")
    
    #input validation
    options = ["1","2","3","4","5","6","7"]
    while(bet_op not in options):
        bet_op=input("Must choose a number 1-7. What bet would you like to place? ")

    print()
    #decide what to do based on user input
    if bet_op == "1":
        print("Place your bet 0-36.")

        #input validation
        while TRUE:
            try:
                bet = int(input("What number? "))
                if bet > 36 or bet < 0:
                    raise ValueError
                break
            except ValueError:
                print("Must be a number between 0-36.")

        any_number(roll(), bet)

    elif bet_op == "2":
        print("Place your bet, red, black or green.")

        #input validation 
        while TRUE:
            try:
                bet = input("What color? ")
                colors = ["red", "black", "green"]
                if bet not in colors:
                    raise ValueError
                break
            except ValueError:
                print("Must be a color red, black or green. case sensitive.")

        red_black(roll(), bet)

    elif bet_op == "3":
        print("Place your bet, even or odd.")

        #input validation 
        while TRUE:
            try:
                bet = input("Which one? ")
                ev_od = ["even", "odd"]
                if bet not in ev_od:
                    raise ValueError
                break
            except ValueError:
                print("Must be even or odd. case sensitive.")

        even_odd(roll(), bet)

    elif bet_op == "4":
        print("\nYou bet the number fell between 1-18.")
        grouped_nums(roll(), bet=1)

    elif bet_op == "5":
        print("\nYou bet the number fell between 19-36.")
        grouped_nums(roll(), bet=2)

    elif bet_op == "6":
        print("Place your bet, column 1-3.")

        #input validation
        while TRUE:
            try:
                bet = int(input("What column? "))
                col_op = [1,2,3]
                if bet not in col_op:
                    raise ValueError
                break
            except ValueError:
                print("Must be a column 1, 2, or 3.")
        
        column_bet(roll(), bet)

    elif bet_op == "7":
        print("Place your bet, row 1-12.")

        #input validation
        while TRUE:
            try:
                bet = int(input("What row? "))
                row_op = [1,2,3,4,5,6,7,8,9,10,11,12]
                if bet not in row_op:
                    raise ValueError
                break
            except ValueError:
                print("Must be a row 1-12. Choose a number in that range.")

        row_bet(roll(), bet)


#print_bet() menu will display user bet options
def print_bet_menu():
    print('''
    Bets
    ----------
    1. any number           (payout 35 to 1)
    2. reds/black/green     (payout 1 to 1)
    3. even/odd             (payout 1 to 1)
    4. fall within 1-18     (payout 1 to 1)
    5. fall within 19-36    (payout 1 to 1)
    6. specific col         (payout 2 to 1)
    7. specific row         (payout 11 to 1)
    ''')
    

#print_menu() will display user options
def print_menu():
    print('''
    Options
    ----------
    1. Place bet
    2. Check Money
    3. Quit
    ''')


""" ===============================================
The main part of the game
Where the user starts!
Sets up board and begins game
=============================================== """
#---main
red = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
black = {2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35}
green = {0}
even = {2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36}
odd = {1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35}

balance = 10 #initial balance user starts with

#print initial setup and menu
print("\n\nWelcome to Roulette! You start with a complimentary balance of $10")
print("-" * 65)
print_menu()
menu_op = input("\nWhat would you like to do? ")

#input validation (initial)
options = ["1","2","3"]
while(menu_op not in options):
    menu_op=input("Must choose a number 1-3. What would you like to do? ")

#run while user still wants to play
while menu_op != "3":
    if balance <= 0:
        print("You have no money. Go find some and come back to play more.")
    elif menu_op == "1":
        make_bet()
    elif menu_op == "2":
        print("\n-------------\nBalance: ${}\n-------------".format(get_balance()))
    
    print_menu()
    menu_op = input("What would you like to do? ")

    #input validation (within loop)
    options = ["1","2","3"]
    while(menu_op not in options):
        menu_op=input("Must choose a number 1-3. What would you like to do? ")

#print final balance
print("\nYou've left today with: ${}\n".format(balance))