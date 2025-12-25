def reverse(n):
    rev = 0
    while n != 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev


num = int(input("enter the number: "))
print("reverse =", reverse(num))
