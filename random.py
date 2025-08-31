def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    print("Prime Number Checker")
    try:
        number = int(input("Enter a number: "))
        if is_prime(number):
            print(f"{number} is a prime number ✅")
        else:
            print(f"{number} is NOT a prime number ❌")
    except ValueError:
        print("Invalid input! Please enter an integer.")
