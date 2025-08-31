def find_candy_count():
    """
    Solves the system of congruences:
    x % 5 == 2
    x % 6 == 3
    x % 7 == 2
    for x < 200.
    """
    max_candy = 200
    print("Solving the Halloween Candy Problem...")
    print("Conditions: x % 5 = 2, x % 6 = 3, x % 7 = 2, x < 200")

    # Iterate through all numbers less than 200
    for x in range(1, max_candy):
        # Check all three conditions
        if (x % 5 == 2) and (x % 6 == 3) and (x % 7 == 2):
            print(f"\nFound solution: {x}")
            print(f"The candy bowl must have {x} pieces of candy!")
            return x

    # If no solution is found
    print(f"\nNo solution found for n < {max_candy}.")
    return None

# This ensures the code runs only when the file is executed directly
if __name__ == "__main__":
    find_candy_count()
