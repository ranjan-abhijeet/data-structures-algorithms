"""
How to find sum of digits of a positive integer number using recursion?

Example: 25 --> 7
"""

def sum_of_digits(number):
    """
    Returns the sum of digits of the integer
    """
    assert type(number) == int and number >= 0, f"Expected positive integer but got {type(number)} {number}"

    if number % 10 == number:
        return number
    else:
        return number % 10 + sum_of_digits(number // 10) 


if __name__ == "__main__":
    print(sum_of_digits(123))