**Recursion**

Recursion is a probelm solving technique in which we call a function again and again until the problem has been solved.

The problems which recursion solves can usually be solved by iterative methods as well. 

Recursion tries to solve a problem by making it smaller and smaller until it reaches an ending or the stopping condition at which point the result is calculated.

**Properties Of Recursion**
1. Performing the same operation multiple times with different inputs.
2. In every step, we try smaller inputs to make the problem smaller.
3. Base or stopping condition is needed to stop the recursion, otherwise we enter infinite loop condition.

**Why Recursion?**
1. Helps in breaking down big problems into smaller ones which are easier to solve. This also makes the code compact and is easier to understand.

2. Trees and graphs data structures use recursion for some of the methods.

3. Recursion is used in many algorithms like divide and conquer algorithms, greedy algorithms, dynamic programming.

*Recursion should be used only when solving the subproblems also involve similar operations as solving the bigger problem.*

**How Recursion Works?**
1. A method to execute an operation on smaller values. Here, the method calls itself on smaller values.
2. An exit condition to get out of loop, this is usually called base condition.
3. Structure of code:
    ```
    def recursion_method(parameters):
        if (base condition):
            return some value
        else:
            recursion_method(modified parameters)
    ```

**Why To Avoid Recursion?**
1. It consumes a lot of memory by storing the function calls in the stack memory.
2. It consumes a lot of time in inserting and removing function calls from the stack memory.
