n = int(input("Enter the number of students: "))

print("Enter the marks:")
for i in range(1, n + 1):
    marks = int(input())

    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 60:
        print("Grade C")
    elif marks >= 40:
        print("Grade D")
    else:
        print("Fail")
