n = int(input("Enter the Num: "))

if n < 100:
    print("Small")
elif n > 100 and n < 200:
    print("Large")
elif n > 201 and n < 300:
    print("Bigger")
elif n > 301 and n < 400:
    print("Largest")
elif n > 400:
    print("Very large")
else:
    print("invalid num")
