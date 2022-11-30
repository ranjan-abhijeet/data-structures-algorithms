"""
Finding the greatest common divisior of two numbers using recursion
"""

def greatest_common_divisor(num1, num2):
    """
    Returns the greates common divisor of the input numbers passed.
    """
    
    assert type(num1) == int and type(num2) == int, f"Expected integer but got {num1} & {num2}"
    
    if num1 < 0: num1 = -1 * num1
    if num2 < 0: num2 = -1 * num2

    if num1 == 0:
        return num2
    
    elif num2 == 0:
        return num1

    else:
        smaller = num1 if num1 <= num2 else num2
        larger = num1 if num1 >= num2 else num2
        return greatest_common_divisor(smaller, larger % smaller)
        
    

if __name__ == "__main__":
    print(greatest_common_divisor(150, -20))