# This is Andrew Xing's file
def encode(password):
    length = len(password)
    i = 0
    afterencoding = ""
    while i < length:
        afterencoding = afterencoding + str((int(password[i]) + 3) % 10)
        i = i + 1
    return afterencoding


if __name__ == "__main__":

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
            pass
        elif option == '3':
            break
