from login import login, logout, register
from expenses import Expense
from budgeter import Profile 

def main():
    curr_user = None
    while True:
        print("Welcome to your personal budgeter. Let's get started!")
        print("Please select from the following options: \n\
              1. New user? Register. \n\
              2. Log-in \n\
              3. Exit")
        selection = int(input("Selection: ")) - 1
        if 0 > selection < 3 :
            print("Invalid selection. Please enter a number between 1 and 3, inclusive.")
        elif selection == 0:
            register()
            entry = input("Would you like to login? Y/N: ")
            if entry == 'Y' or 'y':
                curr_user = login()
                break
            elif entry == 'N' or 'n':
                break
            else:
                print("Invalid selection, please choose Y for yes, or N for no")
        elif selection == 1:
            curr_user = login()
            print(f"Welcome {curr_user}")
            print(type(curr_user))

            
        else:
            break
    


        


if __name__== "__main__":
    main()  