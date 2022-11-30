"""
Fibonacci numbers follow the following rule:
    F(n) = F(n-1) + F(n-2)
    with base conditions: 
        F(0) = 0 
        F(1) = 1
"""

def fibonacci_numbers(number):
    """
    Prints the value of Fibonacci series at given index

    Args:
    series_length   (int)   the length of fibonacci series required.

    Returns:

    """

    assert type(number) == int and number >= 0, f"Number should be positive integer but got {number}"

    if number in [0, 1]:
        return number

    else:
        return fibonacci_numbers(number - 1) + fibonacci_numbers(number - 2)


if __name__ == "__main__":
    print(fibonacci_numbers(10))