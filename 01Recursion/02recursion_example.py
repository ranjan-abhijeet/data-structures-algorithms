"""
Example of how function is called:

How the memory stack looks like for the below function calls:

    fourth()
    --------
    third()
    --------
    second()
    --------
    first()
    --------
"""

def first():
    second()
    print("first method")

def second():
    third()
    print("second method")

def third():
    fourth()
    print("third method")

def fourth():
    print("fourth method")

if __name__ == "__main__":
    first()