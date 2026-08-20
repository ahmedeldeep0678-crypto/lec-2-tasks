numbers = ["10", "5", "abc", "20", "30"]

for value in numbers:
    try:
        number = int(value)

        if number < 10:
            continue

        if number == 30:
            break

        print(number)

    except ValueError:
        continue