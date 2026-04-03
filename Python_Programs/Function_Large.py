def largest(n1, n2):
    if n1 > n2:
        print("No is larger")
    else:
        print("No is smaller")


n1, n2 = map(int, input("enter the two no: ").split())
largest(n1, n2)
