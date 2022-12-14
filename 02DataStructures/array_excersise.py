"""
Following along: https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md
"""
expense_list = [2200, 2350, 2600, 2130, 2190]

"""
1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
"""
ans_1 = expense_list[1] - expense_list[0]

ans_2 = sum(expense_list[:3])
ans_3 = False
for expense in expense_list:
    if expense == 2000:
        ans_3 = True
        break
expense_list.append(1980)
ans_4 = expense_list
expense_list[3] = expense_list[3] - 200
ans_5 = expense_list

"""
1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
"""
heros=['spider man','thor','hulk','iron man','captain america']
#1 
ans_1 = len(heros)
#2 
heros.append('black panther')
#3
heros.pop()
heros.insert(3, 'black panther')
#4
heros[1:3] = ['doctor strange']
#5
heros.sort()
print(heros)

"""
Create a list of all odd numbers between 1 and a max number.
Max number is something you need to take from a user using input() function
"""

def find_max():
    max = int(input("Enter the max number: "))
    odds = []
    for i in range(1, max+1):
        if i % 2 != 0:
            odds.append(i)
    print(odds)

find_max()