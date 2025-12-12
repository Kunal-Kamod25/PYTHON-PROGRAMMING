num = int(input("enter num: "))

ans = 0

while True:
    rem = num % 10
    ans = ans * 10 + rem
    num //= 10
    if num == 0:
        break

print("reversed =", ans)
