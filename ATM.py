balance = 1500  

def BalanceChecking():
    global balance
    print("\nYour current balance is " +str(balance))

def CashWithdrawal():
    global balance  
    print("\nWithdraw Cash")
    amount = float(input("Enter the amount to withdraw: $"))  
    if amount > balance:
        print("Insufficient balance. Transaction failed.")
    elif amount <= 0:
        print("Invalid amount. Please enter a positive number.")
    else:
        balance -= amount
        print("Please take your $"+str(amount)+" cash. New balance: $"+str(balance)+".")

def CashDeposit():
    global balance  
    print("\nDeposit Cash")
    amount = float(input("Enter the amount to deposit: $"))  
    if amount <= 0:
        print("Invalid amount. Please enter a positive number.")
    else:
        balance += amount
        print("Deposit successful. New balance: $"+str(balance)+".")

while True:
        print("\n====================================")
        print("           WELCOME TO ATM          ")
        print("====================================")
        print("[1] Check Balance")
        print("[2] Withdraw Cash")
        print("[3] Deposit Cash")
        print("[4] Exit")
        print("====================================")
        
        option = input("Select an option: ")
        
        if option == "1":
            BalanceChecking()
        elif option == "2":
            CashWithdrawal()
        elif option == "3":
            CashDeposit()
        elif option == "4":
            print("\nSession ended. ")
            print("Thank you for using our ATM. Have a nice day! ")
            input("\nPress Enter to exit...")
            break
        else:
            print("Invalid selection.")






