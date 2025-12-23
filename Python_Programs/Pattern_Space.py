n = int(input("Enter an integer: "))

s = 0
i = 1
tn = n

while i <= n:
    ts = 0
    while ts < s:
        print(" ", end="")
        ts += 1

    j = 1
    while j <= tn:
        print(j, end=" ")
        j += 1

    print()
    s += 2
    tn -= 1
    i += 1
