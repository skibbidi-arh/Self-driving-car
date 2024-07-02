MAX_LINES =3
MAX_BET =100
MIN_BET= 1

def deposit():
    while True:
        amount = input("What would you like to deposit ? ")
        if amount.isdigit():  #the input is always a string. it checks if the entered string is a number digits or not
            amount = int(amount)
            if amount>0 :
                break
            else:
                print("Amount must be greater than 0")

        else: 
            print("Please enter a positive number ")

    return  amount


def get_lines():
    while True:
        lines = input("enter the number of lines to bet on each line? (1-3) ")
        if lines.isdigit():  #the input is always a string. it checks if the entered string is a number digits or not
            lines= int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")

        else: 
            print("Please enter a valid number ")
        
    return lines         

def get_bet():
    while True:
        amount = input("what would you like to bet between "+str(MIN_BET)+" And "+str(MAX_BET)+"-  ")
        if amount.isdigit():  #the input is always a string. it checks if the entered string is a number digits or not
            amount= int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print(f"Amount must be in between ${MIN_BET} and ${MAX_BET}")

        else: 
            print("Please enter a valid number ")
        
    return amount         
    



def main():

 balance = deposit()
 lines = get_lines()
 bet = get_bet()


main()