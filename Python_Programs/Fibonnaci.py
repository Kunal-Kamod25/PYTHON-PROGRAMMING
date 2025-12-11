n = int(input("Enter a number: "))

i = 1
f1 = 1
f2 = 1
sum_val = 0

while f1 < n:
    if f1 % 5 == 0:
        sum_val += f1

    print(f1, end=" ")

    f3 = f1 + f2
    f1 = f2
    f2 = f3

print("\nsum is", sum_val)
