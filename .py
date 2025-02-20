def calculate_factorial(n):
    # Function to calculate the factorial of a given number using a for loop
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def main():
    # Main function to run the program
    print("Welcome to the Factorial Calculation program!")
    while True:
        try:
            n = int(input("Which factorial would you like to calculate? "))
            if n < 0:
                print("Please enter a non-negative integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")
    
    result = calculate_factorial(n)
    print(f"The factorial of {n} is {result}")

if __name__ == "__main__":
    main()
