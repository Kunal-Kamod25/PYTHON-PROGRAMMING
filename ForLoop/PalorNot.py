num = int(input("Enter an Integer: "))
original = num
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

print("Original Number:", original)
print("Reverse of Number:", rev)

if original == rev:
    print("Number is palindrome.")
else:
    print("Number is not palindrome.")

