a, b, c = map(float, input("enter the triangle lengths: ").split())

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("is equilateral")
    elif a == b or b == c or a == c:
        print("is isosceles")
    else:
        print("is scalene")
else:
    print("not valid triangle")
