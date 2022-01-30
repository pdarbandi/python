# Assignment 1:
"""
    Create a function named merge_lists that accepts 2 lists.
    The function is supposed to merge both of those lists together
    and return the result.
"""

# your code below:

my_list1 = [1,2,3]
my_list2 = [4,5,6]

def merge_lists(list1, list2):
    return list1 + list2


my_final_list = merge_lists(my_list1, my_list2)

print(my_final_list)


my_list = merge_lists([1,2,3],['a', 'b', 'c'])
print(my_list)

print(merge_lists([1,2,3],['a', 'b', 'c']))




































# solution Below:

# def merge_lists(list_a, list_b):
#     return list_a + list_b
#
# my_list = merge_lists([1,2,3],['a', 'b', 'c'])
# print(my_list)