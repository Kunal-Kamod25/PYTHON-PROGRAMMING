n = int(input("Enter a integer: "))

count = 0
total = 0.0

for i in range(n):
    num = float(input("enter num: "))
    if num > 0:
        total += num
        count += 1

if count > 0:
    print("Average =", total / count)
else:
    print("Non positive num")
