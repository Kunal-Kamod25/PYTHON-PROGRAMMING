while True:
    op = input("enter the operator (-,+,*,/, or 4 to exit): ")

    if op == '4':   # exit condition
        break

    n1 = int(input("enter number 1: "))
    n2 = int(input("enter number 2: "))

    if op == '+':
        print("addition is =", n1 + n2)
    elif op == '-':
        print("subtraction is =", n1 - n2)
    elif op == '*':
        print("multiplication is =", n1 * n2)
    elif op == '/':
        if n2 != 0:
            print("division is =", n1 // n2)   # integer division like in C
        else:
            print("division by zero error")
    else:
        print("invalid operation")
