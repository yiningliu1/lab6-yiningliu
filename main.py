# function to encode a password
def encode(password):
    key = "3456789012"
    encoded_password = ""
    for i in password:
        i = int(i)
        encoded_password += key[i]
    return encoded_password


def main():
    # loop that prints menu until user quits
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("Please enter an option: ")
        # encodes and stores the password if user picks "1"
        if option == "1":
            password = input("Please enter your password to encode: ")
            password = encode(password)
            print("Your password has been encoded and stored")
        # prints out the decoded password if user picks "2"
        if option == "2":
            print(f"The encoded password is {password}, and the original password is {decode(password)}")
        # breaks the loop is user picks "3"
        if option == "3":
            break


if __name__ == "__main__":
    main()
