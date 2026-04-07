correct_name = "admin"
correct_password = "1234"
balance = 500

name = input("Enter username: ")
password = input("Enter password: ")

while name != correct_name or password != correct_password:
    print ("Access Denied. Try again")
    name = input("Enter username: ")
    password = input("Enter password: ")

print("Login Successful")


print("Choose one option:")
print("1 - Check balance")
print("2 - Deposit money")
print("3 - Withdraw money")

choice = input("Enter choice: ")


if choice == "1":
        print("Your current balance is:", balance)

    
elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print("Deposit successful!")
        print("Your new balance is:", balance)
        
elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawn Successful!")
            print("Updated  balance: ", balance)
        else:
            print("Insufficient balance")
            print("Your current balance is: ", balance)

else:
        print("Invalid option")