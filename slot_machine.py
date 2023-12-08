# Project with techwithtim


import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# 5 peach, 4 aubergine, 3 Jizz, 2 stars, 1 CUM



symbol_count = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
    "J": 1
}

symbol_value = {
    "A": 1,
    "B": 2,
    "C": 5,
    "D": 20,
    "J": 100
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line] #check the first symbol
        for column in columns: # loop trough all columns to check if it is the same symbol
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
            
    return winnings, winning_lines


def get_slot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): #Eg: "A" "5"
        for _ in range(symbol_count): # The range is thus 2
            all_symbols.append(symbol) #So it appends "A" two times
            
    columns = []
    for _ in range(cols): # As we have 3 columns, we need to execute the following code three times
        column = []
        current_symbols = all_symbols[:] # the brakets creates a copy otherwise reference
        for _ in range(rows): # as we have 5 rows, we need 5 symbols per column thus iterate through number of rows
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
    return columns

def print_slot(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], "|", end=" | ")
            else:
                print(column[row], "|", end ="")
                
        print()

def deposit():
    #collects user input that gets the deposite
    # funtion is a selection of code that can return a certain value
    while True:
        amount = input("What would you like to deposite? $")
        if amount.isdigit(): # makes sure that responds is a number
            amount = int(amount)
            if amount > 0:
                break # if yes we break out of the if statement
            else: 
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")?")
        if lines.isdigit(): # makes sure that responds is a number
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break # if yes we break out of the if statement
            else: 
                print("Enter valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit(): # makes sure that responds is a number
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break # if yes we break out of the if statement
            else: 
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is: ${balance} ")
        else:
            break
            
    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_spin(ROWS, COLS, symbol_count)
    print_slot(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet



def main(): # by defining this as a function we can always call the above code
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input ("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")


    
main()

