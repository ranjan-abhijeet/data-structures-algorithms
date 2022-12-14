"""
Program with time complexity of order 2 
"""

def squaring_array(number_list):
    squared_list = []
    for num in number_list:
        squared_list.append(num*num)
    return squared_list
