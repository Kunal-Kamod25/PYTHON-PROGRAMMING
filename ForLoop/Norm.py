import math

real = float(input("Enter real part: "))
imag = float(input("Enter imaginary part: "))

norm = math.sqrt(real * real + imag * imag)
print("norm =", norm)
