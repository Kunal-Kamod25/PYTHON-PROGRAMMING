n = int(input("Enter the Num: "))

if n < 100:
    print("small")
elif n > 100 and n < 200:
    print("large")
elif n > 201 and n < 300:
    print("bigger")
elif n > 301 and n < 400:
    print("largest")
elif n > 400:
    print("very large")
else:
    print("invalid num")
