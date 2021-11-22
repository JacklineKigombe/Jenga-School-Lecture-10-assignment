n=int(input("Enter the number to print the tables for: "))
for i in range(1,11):
    print(str(i) + "\t" + str(n**i) + "\t" + str(format(float(1/i),".3f")))
