"""
Given a number x and power n, return (x)^n or x**n
"""

def power_of_number(base, exponent):
    """
    Returns the value base ** exponent using recursion
    """
    
    assert base != 0 and type(base) == int and type(exponent) == int, f"""got number {number} and power {power}."""

    if exponent == 0:
        return 1

    elif exponent < 0:
        return 1/base * power_of_number(base, exponent + 1)

    else:
        return base * power_of_number(base, exponent - 1)


if __name__ == "__main__":
    print(power_of_number(4, -1))
    print(power_of_number(3, 3))
    print(power_of_number(-2, 4))