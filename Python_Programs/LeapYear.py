Year = int(input("Enter the year: "))
if (Year % 400 == 0) and (Year % 100 == 0):
    print(f"{Year} is a Leap Year")
elif (Year % 4 == 0) and (Year % 100 != 0):
    print(f"{Year} is a Leap Year")
else:
    print(f"{Year} is not a Leap Year")