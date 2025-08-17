balance = 5000
# pin = "1290"
pin = input("Set Your 4-digit ATM PIN:")
transactions = []

print("----- Welcome to Titan ATM -----")

attempts = 0
while attempts < 3:
    user_pin = input("Enter your 4-digit PIN: ")
    if user_pin == pin:
        print("Login Successful \n")
        break
    else:
        attempts += 1
        print(f"Wrong PIN! Attempts left: {3 - attempts}")

if attempts == 3:
    print(" Your ATM card is blocked due to 3 wrong attempts.")
    exit()

while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Mini Statement")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print(f"Your balance is: {balance}")

    elif choice == "2":
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        transactions.append(f"Deposited {amount}")
        print(f"{amount} deposited successfully! New Balance: {balance}")

    elif choice == "3":
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            transactions.append(f"Withdrew {amount}")
            print(f"{amount} withdrawn successfully! Remaining Balance: {balance}")
        else:
            print("Insufficient Balance!")

    elif choice == "4":
        print("\n----- Mini Statement -----")
        if not transactions:
            print("No transactions yet.")
        else:
            for t in transactions[-5:]:
                print(t)
        print(f"Available Balance: {balance}")

    elif choice == "5":
        print("Thank you for using Titan ATM! ")
        break

    else:
        print("Invalid Choice! Please try again.")