num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Function to calculate sum of proper divisors
def sum_of_divisors(n):
    total = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            total += i
    return total

# Calculate sums
ans1 = sum_of_divisors(num1)
ans2 = sum_of_divisors(num2)

# Check amicable condition
if ans1 == num2 and ans2 == num1:
    print(num1, "and", num2, "are amicable numbers")
else:
    print(num1, "and", num2, "are not amicable numbers")
