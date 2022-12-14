"""
Converting a number from Decimal to Binary using recursion
"""

def decimal_to_binary(decimal_number):
    """
    Returns the binary(base 2) representation of the decimal(base 10) number
    """
    assert type(decimal_number) == int, f"Expected integer but received {decimal_number}"
    if decimal_number == 0:
        return 0
    else:
        return decimal_number % 2 + decimal_to_binary(int(decimal_number / 2)) * 10


if __name__=="__main__":
    print(decimal_to_binary(13))
    print(decimal_to_binary(-24))