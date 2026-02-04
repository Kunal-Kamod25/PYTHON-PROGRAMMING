Num = (input("Enter three numbers separated by Space: ")).split()
if (int(Num[0]) >= int(Num[1])) and (int(Num[0]) >= int(Num[2])):
    print(f"Largest number is {Num[0]}")
elif (int(Num[1]) >= int(Num[0])) and (int(Num[1]) >= int(Num[2])):
    print(f"Largest number is {Num[1]}")
else:

    print(f"Largest number is {Num[2]}")
