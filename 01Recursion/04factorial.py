"""
Function to return factorial of a given number using recursion.
Factorial is product of all positive integers less than or equal to n.
"""

def factorial(number):
    """
    Returns the factorial of input

    Args:
    number (int)    the number of which factorial is required

    Returns:
    (int) factorial of the given number
    """
    assert number >= 0 and type(number) == int, f"Expected positive integer but got value {number}"

    if number in [0, 1]:
        return 1

    else:
        return number * factorial(number - 1)
    

if __name__ == "__main__":
    print(factorial(5))