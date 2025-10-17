try:
    n = int(input("Enter a number: "))

    # Loop from 0 up to and including the number n
    for i in range(n + 1):
        # Check if the number is even
        if i % 2 == 0:
            print(f"{i} is Even")
        # Otherwise, the number is odd
        else:
            print(f"{i} is Odd")
            
except ValueError:
    print("Invalid input. Please enter an integer.")