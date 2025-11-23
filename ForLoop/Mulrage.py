num = int(input("Enter the number: "))

if num < 100:
    print("Small")
elif 100 <= num <= 200:
    print("Large")
elif 201 <= num <= 300:
    print("Bigger")
elif 301 <= num <= 400:
    print("Largest")
else:
    print("Very Large")
