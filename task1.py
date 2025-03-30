def check_even_odd():
    try:
        # Taking integer input from the user
        num = int(input("Enter an integer: "))

        # Checking if the number is even or odd
        if num % 2 == 0:
            print(f"{num} is an Even number.")
        else:
            print(f"{num} is an Odd number.")

    except ValueError:
        print("Error: Please enter a valid integer.")

# Run the function
if __name__ == "__main__":
    check_even_odd()
