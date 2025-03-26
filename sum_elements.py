# A refactored program to calculate the sum of user-provided integers.

MAX = 100

def calculate_sum(numbers):
    """Calculate the sum of a list of numbers."""
    return sum(numbers)

def get_integer_input(prompt):
    """Prompt the user for an integer input and handle invalid input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    """Main function to execute the program."""
    try:
        n = get_integer_input("Enter the number of elements (1-100): ")
        if not 1 <= n <= MAX:
            print(f"Invalid input. Please provide a number between 1 and {MAX}.")
            return

        print(f"Enter {n} integers:")
        numbers = [get_integer_input(f"Element {_ + 1}: ") for _ in range(n)]

        total = calculate_sum(numbers)
        print("Sum of the numbers:", total)

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
