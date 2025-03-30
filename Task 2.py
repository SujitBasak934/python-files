def sum_numbers():
    # Calculating sum of numbers from 1 to 50 using a loop
    total_sum = 0
    for num in range(1, 51):
        total_sum += num

    # Displaying the final sum
    print(f"The sum of integers from 1 to 50 is: {total_sum}")

# Run the function
if __name__ == "__main__":
    sum_numbers()
