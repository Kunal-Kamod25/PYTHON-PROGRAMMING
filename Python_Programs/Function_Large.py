def largest(n1, n2):
    if n1 > n2:
        print("no is larger")
    else:
        print("no is smaller")


n1, n2 = map(int, input("enter the two no: ").split())
largest(n1, n2)
