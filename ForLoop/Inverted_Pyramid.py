n = int(input("enter an integer: "))

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
    tn -= 1
    s += 1
    i += 1
