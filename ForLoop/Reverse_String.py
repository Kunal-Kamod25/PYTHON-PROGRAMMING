num = int(input("Enter an Integer: "))
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

print("Reverse of number:", rev)

