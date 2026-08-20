day = input("Enter a day: ")

match day:
    case "Saturday":
        print("Weekend")
    case "Sunday":
        print("Weekend")
    case "Monday":
        print("Work day")
    case "Tuesday":
        print("Work day")
    case "Wednesday":
        print("Work day")
    case _:
        print("Unknown day")