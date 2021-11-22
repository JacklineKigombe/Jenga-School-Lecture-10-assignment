#Replacing each character with the corresponding character that is 5 times ahead

def main ():
    message = input("Please enter the message to encode: ")

    for ch in message:
        print(chr(ord(ch) + 5), end=" ")

main()
