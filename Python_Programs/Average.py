def main():
    try:
        n = int(input("enter a num: "))
    except ValueError:
        print("Invalid integer.")
        return

    if n <= 0:
        print("n must be a positive integer.")
        return

    A = []
    print("enter array elements:")
    for _ in range(n):
        try:
            A.append(int(input()))
        except ValueError:
            print("Invalid integer. Exiting.")
            return

    total = sum(A)
    print(f"sum={total}")
    print(f"average of the array elements={total / n}")

if __name__ == "__main__":
    main()
