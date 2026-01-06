age = int(input("Enter the Alien age: "))

if age < 5:
    print("Infant")
elif age >= 5 and age <= 50:
    print("Teenager")
elif age >= 51 and age <= 300:
    print("Adult")
elif age > 300:
    print("Ancient")
else:
    print("Invalid age")
