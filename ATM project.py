correct_name = "admin"
correct_password = "1234"
balance = 1000


def login():
    name = input("Enter username: ")
    password = input("Enter password: ")

    while name != correct_name or password != correct_password:
        print("Access Denied. Try again")
        name = input("Enter username: ")
        password = input("Enter password: ")

    print("Login Successful")


def menu():
    print("Choose one option:")
    print("1 - Check balance")
    print("2 - Deposit money")
    print("3 - Withdraw money")


def check_balance():
    return balance



def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Deposit successful!")



def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Withdraw Successful!")
    else:
        print("Insufficient balance")


login()
menu()

choice = input("Enter choice: ")

if choice == "1":
    print("Your current balance is:", check_balance())
elif choice == "2":
    deposit()
    print("Your new balance is:", balance)
elif choice == "3":
    withdraw()
    print("Your current balance is:", balance)
else:
    print("Invalid option")