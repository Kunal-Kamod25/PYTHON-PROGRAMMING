num = int(input("enter a number: "))

if num < 10:
    check = 1
elif num == 10:
    check = 2
else:
    check = 3

if check == 1:
    print("small")
elif check == 2:
    print("equal")
elif check == 3:
    print("larger")
