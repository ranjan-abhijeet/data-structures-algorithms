"""
Program with order 1 execution time
"""

def find_pe_for_index(price_list, eps_list, index):
    pe = price_list[index]/eps_list[index]
    return pe

price_list = [i for i in range(500, 600)]
eps_list = [i for i in range(100, 200)]

if len(price_list) == len(eps_list):
    print(find_pe_for_index(price_list, eps_list, 10))