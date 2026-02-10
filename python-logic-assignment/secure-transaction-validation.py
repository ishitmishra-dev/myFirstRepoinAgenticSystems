# Take inputs
balance = int(input("Enter account balance: "))
withdrawal_amount = int(input("Enter withdrawal amount: "))
verified_input = input("Is the account verified? (True/False): ").strip().lower()

# Convert verification input to Boolean
if verified_input == "true":
    is_verified = True
elif verified_input == "false":
    is_verified = False
else:
    print("Invalid verification input")
    exit()

# Transaction validation using compound Boolean expression
if is_verified and withdrawal_amount <= balance:
    print("Withdrawal successful")
else:
    print("Transaction denied")
