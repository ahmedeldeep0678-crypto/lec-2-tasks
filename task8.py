students = ["Ahmed", "Omara", "Ali", "Youssef", "Eldeep"]
passed = [True, False, True, True, False]

for i in range(len(students)):
    if passed[i]:
        print(students[i], "passed")
    else:
        print(students[i], "failed")