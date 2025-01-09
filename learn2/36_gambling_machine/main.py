import random   #bedziemy losowo generowac wynik "slot machine"
#from traceback import print_tb

MAX_LINES=3  #wartości stałe(constant wpisujemy wielkimi literami)
MAX_BET = 100
MIN_BET = 1

ROWS=3  #definiujemy rozmiar maszyny losującej
COLS=3

symbol_count={     #generujemy ilość znaków w
                    # każdej linii maszyny
    "A":2,             #to jest SŁOWNIK
    "B":4,
    "C":6,
    "D":8
}

symbol_value={
    "A":5,             #to jest SŁOWNIK
    "B":4,
    "C":2,
    "D":2
}

def check_winnings(columns, lines, bet,values):
    winnings= 0
    winning_lines=[]
    for line in range(lines):
        symbol= columns[0][line]
        for column in columns:
            symbol_to_check= columns[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet

    return winnings

def get_slot_machine_spin(rows,cols,symbols): #ta funkcja będzie losować symbole do 3 rzędów w 3 kolumnach
    all_symbols = []  #tworzymy listę w której są wszystkie symbole z której będziemy 3 losowe elementy
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count): #underscore to anonimowa zmienna, dzieki temu nie marnujemy znaków na jakieś inne ważniejsze zmienne
            all_symbols.append(symbol)

    columns =  []
    for _ in range(cols): #dla każdej kolumny(których mamy zdeklarowanych 3) muszę petlą wygenerować tyle symboli ile jest rzędów
        column=[]
        current_symbols=all_symbols[:] #[:] kopiuje wartości z all_symbols do current_symbols- chodzi o to że dla każdej
        for _ in range(rows):           #kolummy losujemy z nowej instacji listy all symbols. all symbols to lista
            value= random.choice(current_symbols) # wszystkich znaków jakie mogą się pojawić w kolumnie, jeśli wykorzystam w
            current_symbols.remove(value)    #pierwszej kolumnie np. 2 znaki A i 1 B to chcę mieć możliwość wykorzystania tych samych znaków w kolejnej kolumnie. dlatego kopiuję
            columns.append(value) #tutaj nastepuje usuniecie wykorzystanego symbolu

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ") #generuję separator na konczy kazdej kolumny
            else:
                print(column[row], end="")
        print()

def deposit():
    while True: #petla while działa dopóki z niej nie wyjdziemy funkcją break
        amount = input("What would You like to deposit $ ")
        if amount.isdigit(): #walidacja inputu: czy to liczba?
            amount= int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on(1-" + str(MAX_LINES)+ ")? ")
        if lines.isdigit():
            lines= int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    while True:
        amount = input("What would You like to bet on each line? $ ")
        if amount.isdigit():
            amount= int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def main():
    balance= deposit()
    lines= get_number_of_lines()
    while True: #ta pętla sprawdza czy mamy wystarczającą ilość pieniędzy
        bet= get_bet()
        total_bet=bet*lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: $ {balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots= get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings= check_winnings(slots,lines,bet,symbol_value)
    print(f"You won ${winnings}.")

main()