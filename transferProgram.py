# TRANSFER PAGE PROGRAM (@emeka_io on X)
print('Transfer Page')
print("What kind of transaction are you making? ")
trans_type = input("Crypto or Regular: ")
if trans_type == 'regular':
    print("Select Bank")
    bank = input("Enter Bank Name e.g FirstBank: ")
    print("Account Number")
    acc_num = int(input("Enter the account number: "))

     # TRANSFER CONFIRMATION
    print(f"Are you sure you want to make a transfer to '{bank}', '{acc_num}' ? ")
    ans = input("Yes or No: ")
    if ans == 'yes':
        print("Ok, your transfer has been initiated.")
    elif ans == 'no':
        print("OK, transfer has been cancelled.")
    else:
         print("Invalid Input, Try again.")
# CRYPTO TRANSFER
elif trans_type == 'crypto':
    print("Select Cryptocurrency")
    crypto = input("Enter Crypto type e.g FirstBank: ")
    print("Wallet Address")
    wal_add = input("Enter Wallet address: ")

    # TRANSFER CONFIRMATION
    print(f"Are you sure you want to make a transfer to '{crypto}', '{wal_add}' ? ")
    ans = input("Yes or No: ")
    if ans == 'yes':
        print("Ok, your transfer has been initiated.")
    elif ans == 'no':
        print("OK, transfer has been cancelled.")
    else:
         print("Invalid Input, Try again.")
else:
    print("Invalid Input, Try again.")

print("Thanks for using EMEKA BANK")

