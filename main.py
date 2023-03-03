def mobile_money():
    minimum_balance = 3000
    current_balance = minimum_balance
    deposit = 0

    while True:
        print("\nWelcome to MTN Mobile Money!!\n1. Deposit money\n2. Check balance\n3. Withdraw money\n0. Exit")
        option = int(input("Select an option: "))

        if option == 1:
            amount = int(input("Enter the amount you want to deposit in GHS: "))
            if amount <= 0:
                print("Invalid amount. You should deposit an amount greater than 0.")
            else:
                deposit += amount
                current_balance = minimum_balance + deposit
                print("You have deposited GHS %d and your current balance is GHS %d." % (amount, current_balance))

        elif option == 2:
            print("Your current balance is GHS %d." % current_balance)

        elif option == 3:
            amount = int(input("Enter the amount you want to withdraw in GHS: "))
            if amount <= 0:
                print("Invalid amount. You should withdraw an amount greater than 0.")
            elif amount > current_balance:
                print("Insufficient funds. You cannot withdraw more than your current balance.")
            elif amount < minimum_balance:
                print(
                    "Invalid amount. You should withdraw an amount greater than or equal to GHS %d." % minimum_balance)
            else:
                current_balance -= amount
                print("You have withdrawn GHS %d. Your current balance is GHS %d." % (amount, current_balance))

        elif option == 0:
            break

        else:
            print("Unknown option. Please select a valid option.")
