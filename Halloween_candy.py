def find_candy_count(max_candy):
    """
    Solves the system of congruences:
    x % 5 == 2
    x % 6 == 3
    x % 7 == 2
    for x < max_candy.
    """
    print("Solving the Halloween Candy Problem...")
    print(f"Conditions: x % 5 = 2, x % 6 = 3, x % 7 = 2, x < {max_candy}")

    # Iterate through all numbers less than max_candy
    for x in range(1, max_candy):
        # Check all three conditions
        if (x % 5 == 2) and (x % 6 == 3) and (x % 7 == 2):
            print(f"\nFound solution: {x}")
            print(f"The candy bowl must have {x} pieces of candy!")
            return x

    # If no solution is found
    print(f"\nNo solution found for n < {max_candy}.")
    return None


if __name__ == "__main__":
    # Ask user for maximum candy limit
    try:
        max_candy = int(input("Enter the maximum number of candies to check: "))
        find_candy_count(max_candy)
    except ValueError:
        print("Please enter a valid integer.")
