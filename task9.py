number = int(input("Enter a number: "))

if number > 0:
    for i in range(1, number + 1):
        print(i)
else:
    print("Enter a positive number")