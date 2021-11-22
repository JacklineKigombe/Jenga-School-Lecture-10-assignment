#Multiplication then covert to string then print each character in a new line

def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    #Find product
    c = str(a * b)
    for ch in c:
        print(ch)
    
main()
