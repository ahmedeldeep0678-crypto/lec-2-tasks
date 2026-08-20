values = ["10", "25", "abc", "40", "15"]

for value in values:
    try:
        number = int(value)

        if number % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")

    except ValueError:
        print(f"{value} is not a valid number")