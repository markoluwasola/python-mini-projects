#The ATM Simulator
#This program simulates an ATM machine. It allows the user to check their balance, deposit money, withdraw money and exist.
available_balance = 100.00
while True:
    user_name = input("Please enter your username:")
    password = input("Please enter your password: ")
    if user_name == "Markllll" and password == "1234":
        print("Welcome to the ATM Simulator, Markllll!")
        action = input("what would you like to do today? \n1. Check Balance \n2. Deposit Money \n3. Withdraw Money \n4. Exit \nplease enter the number corresponding to your choies:  ")
        if action == "1":
            print("Your current balance is $:", round(available_balance,2))
            print("Thank you for using the ATM Simulator. Don't forget to take your card! \nHave a great day!")
            break
        elif action == "2":
            while True:
                deposit_amount = input("How much would you like to deposit? $")
                try: 
                    deposit_amount = float(deposit_amount)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            available_balance = available_balance + deposit_amount
            print("Your new balance is: $", round(available_balance,2))
            print("Thank you for using the ATM Simulator. Don't forget to take your card! \nHave a great day!")
        elif action == "3":
            pin = input("Please enter your PIN: ")
            try:
                pin = int(pin)
            except ValueError:
                print("Invalid PIN. Please enter a valid 4-digit PIN.")
                continue
            if pin == 1990:
                print("PIN verified.")
                withdraw_amount = input("How much would you like to withdraw? $")
                try:
                    withdraw_amount = float(withdraw_amount)
                except ValueError:
                    print("invalid input. Please enter a valid number.")
                    continue
                    
                if withdraw_amount > available_balance:
                    print("Insufficient funds. your current balance is $:", round(available_balance,2))
                else: 
                    available_balance = available_balance - withdraw_amount
                    print("Your new balance is: $", round(available_balance,2))
                    print("Thank you for using the ATM Simulator. Don't forget to take your card! \nHave a great day!")
                    
            else:
                print("Invalid PIN.")
        elif action == "4":
            print("Thank you for using the ATM Simulator. Don't forget to take your card! \nHave a great day!")
            break
    else:
        print("Invalid username or password. Please try again.")
        break

