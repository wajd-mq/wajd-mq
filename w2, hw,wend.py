exams = int(input("How many exam grades does each student have? "))
while True:
    print("Enter the exam grades.")
    total = 0
    for i in range(1, exams + 1):
        grades = float(input(f"Exam {i}: "))
        total += grades
    average = total / exams
    print("The average is:", round(average, 2))
    more_stu = input("Enter exam grades for another student (Y/N)? ").lower()
    if more_stu != 'y':
        break