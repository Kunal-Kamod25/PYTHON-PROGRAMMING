n = int(input("Enter the Num: "))

count = 0

if n == 0:
    count = 1
else:
    while n != 0:
        count += 1
        n //= 10

print("Digit =", count)
