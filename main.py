# This is Andrew Xing's file
def encode(password):
    length = len(password)
    i = 0
    afterencoding = ""
    while i < length:
        afterencoding = afterencoding + str((int(password[i]) + 3) % 10)
        i = i + 1
    return afterencoding

def decode(encoded_password):
    length = len(encoded_password)
    i = 0
    afterdecoding = ""
    while i < length:
        afterdecoding = afterdecoding + str((int(encoded_password[i]) - 3) % 10)
        i = i + 1
    return afterdecoding

if __name__ == "__main__":

    encoded = None  # Initialize encoded variable to store the encoded password
    original = None  # Initialize original variable to store the original password

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("Please enter an option: ")

        if option == '1':
            original = input("Please enter your password to encode: ")
            encoded = encode(original)
            if encoded:
                print("Your password has been encoded and stored!")
        elif option == '2':
            if encoded:  # Ensure a password has been encoded before attempting to decode
                decoded = decode(encoded)
                print(f"The encoded password is {encoded}, and the original password is {decoded}.")
            else:
                print("No password has been encoded yet.")
        elif option == '3':
            break