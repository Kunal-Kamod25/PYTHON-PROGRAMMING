def main():
    n = int(input("Enter an integer: "))

    # Read array elements
    A = []
    print("Enter array elements:")
    for i in range(n):
        A.append(int(input()))

    # Print entered array
    print("The entered array is:")
    for num in A:
        print(num, end=" ")

    # Calculate sum
    total = sum(A)
    print(f"\nSum: {total}")

    # Calculate average
    avg = total / n if n > 0 else 0
    print(f"Average: {avg:.2f}")


if __name__ == "__main__":
    main()
