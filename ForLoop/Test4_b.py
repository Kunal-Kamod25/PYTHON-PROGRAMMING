n=int(input("Enter number of elements: "))
row = 0
while row < n:
    col=1
    while col<= n-row:
        print(col, end=" ");
        col=col+1
    print()
    row=row+1
