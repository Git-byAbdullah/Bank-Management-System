def banking_system():
    accounts = {}

    while True:
        print("\n===== BANKING SYSTEM =====")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            acc_num = input("Enter account number: ").strip()
            if acc_num in accounts:
                print("Account already exists.")
                continue
            name = input("Enter customer name: ").strip()
            pin = input("Enter PIN: ").strip()
            try:
                balance = float(input("Enter initial balance: "))
                if balance < 0:
                    print("Initial balance cannot be negative.")
                    continue
            except ValueError:
                print("Invalid amount.")
                continue

            accounts[acc_num] = {
                "name": name,
                "pin": pin,
                "balance": balance,
                "transactions": [f"Account created with initial balance: Rs.{balance:.2f}"]
            }
            print("Account created successfully!")

        elif choice == "2":
            acc_num = input("Enter account number: ").strip()
            pin = input("Enter PIN: ").strip()

            if acc_num in accounts and accounts[acc_num]["pin"] == pin:
                print(f"\nWelcome back, {accounts[acc_num]['name']}!")
                while True:
                    print("\n===== ACCOUNT MENU =====")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Transaction History")
                    print("5. Account Details")
                    print("6. Logout")
                    acc_choice = input("Enter choice: ").strip()

                    account = accounts[acc_num]

                    if acc_choice == "1":
                        try:
                            amount = float(input("Enter amount to deposit: "))
                            if amount <= 0:
                                print("Amount must be greater than zero.")
                                continue
                            account["balance"] += amount
                            account["transactions"].append(f"Deposited: Rs.{amount:.2f}")
                            print(f"Successfully deposited Rs.{amount:.2f}")
                        except ValueError:
                            print("Invalid amount.")

                    elif acc_choice == "2":
                        try:
                            amount = float(input("Enter amount to withdraw: "))
                            if amount <= 0:
                                print("Amount must be greater than zero.")
                                continue
                            if amount > account["balance"]:
                                print("Insufficient balance!")
                            else:
                                account["balance"] -= amount
                                account["transactions"].append(f"Withdrew: Rs.{amount:.2f}")
                                print(f"Successfully withdrew Rs.{amount:.2f}")
                        except ValueError:
                            print("Invalid amount.")

                    elif acc_choice == "3":
                        print(f"Current Balance: Rs.{account['balance']:.2f}")

                    elif acc_choice == "4":
                        print("\n--- Transaction History ---")
                        if not account["transactions"]:
                            print("No transactions yet.")
                        else:
                            for tx in account["transactions"]:
                                print(f"- {tx}")

                    elif acc_choice == "5":
                        print("\n--- Account Details ---")
                        print(f"Name: {account['name']}")
                        print(f"Account Number: {acc_num}")
                        print(f"Current Balance: Rs.{account['balance']:.2f}")

                    elif acc_choice == "6":
                        print("Logged out successfully.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid account number or PIN.")

        elif choice == "3":
            print("Thank you for using the banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    banking_system()