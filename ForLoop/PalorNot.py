num = int(input("Enter an integer: "))
original = num
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

print("Original number:", original)
print("Reverse of number:", rev)

if original == rev:
    print("Number is palindrome.")
else:
    print("Number is not palindrome.")
