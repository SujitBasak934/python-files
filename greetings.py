def main():
    # Taking first name and last name as input
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()

    # Concatenating full name
    full_name = f"{first_name} {last_name}"

    # Printing a personalized greeting message
    print(f"\nHello, {full_name}! Welcome to the Python programming world!")

if __name__ == "__main__":
    main()
