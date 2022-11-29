"""
How the function call is managed in the stack memory:

        -------------------
        print("n is less than 1")
        -------------------
        recursion_example(1)
        -------------------
        recursion_example(2)
        -------------------
        recursion_example(3)
        -------------------
        recursion_example(4)
        -------------------
"""

def recursion_example(n):
    if n < 1:
        print("n is less than 1")
        return
    else:
        recursion_example(n-1)
        print(n)

if __name__ == "__main__":
    recursion_example(4)