n = int(input("enter number: "))

temp = n
ans = 0

while n > 0:
    rem = n % 10
    ans = ans * 10 + rem
    n //= 10

if temp == ans:
    print("palindrome")
else:
    print("not palindrome")
