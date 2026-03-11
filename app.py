# ---------------------------------------------------------
# Python Program to Print Odd Numbers
# This program demonstrates how to print odd numbers
# between a given range using functions and loops.
# ---------------------------------------------------------

# Function to check whether a number is odd
def check_if_odd(number):
    """
    This function checks if a number is odd.
    It returns True if the number is odd,
    otherwise it returns False.
    """
    if number % 2 != 0:
        return True
    else:
        return False


# Function to print odd numbers in a range
def print_odd_numbers(start, end):
    """
    This function prints odd numbers between
    the start and end range.
    """

    print("Printing odd numbers from", start, "to", end)
    print("------------------------------------------")

    for num in range(start, end + 1):

        # Check if number is odd using the function
        if check_if_odd(num):
            print("Odd Number Found:", num)

    print("------------------------------------------")
    print("Finished printing odd numbers.")


# Main function of the program
def main():

    print("Welcome to the Odd Number Generator Program")
    print("-------------------------------------------")

    # Taking input from the user
    start_number = int(input("Enter the starting number: "))
    end_number = int(input("Enter the ending number: "))

    # Calling the function to print odd numbers
    print_odd_numbers(start_number, end_number)

    print("Program executed successfully.")


# Program execution starts here
if __name__ == "__main__":
    main()
