import math

real = float(input("enter real part: "))
imag = float(input("enter imaginary part: "))

norm = math.sqrt(real * real + imag * imag)
print("norm =", norm)
