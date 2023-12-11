"""
Exercise-1: Count unique elements
Write a function "count_unique_elements(my_list: list) -> int" that takes a 
list of integers and returns the number of unique elements in the list.

Example:
count_unique_elements([1, 2, 3, 1, 2, 4, 5, 4]) -> 5
"""



def count_unique_elements(my_list: list) -> int: 
    cnt = 0
    temp = -1
    my_list.sort()
    for i in range(0, len(my_list)):
        if my_list[i] != temp:
            cnt+=1
            temp = my_list[i]
    return cnt

# print(count_unique_elements([1, 2, 3, 1, 2, 4, 5, 4]))
    

"""
Exercise-2: Remove duplicates
Write a function "remove_duplicates(my_list: list) -> list" that takes a list of integers and 
removes all duplicates, returning the new list with unique elements in their original order.

Example:
remove_duplicates([1, 2, 3, 1, 2, 4, 5, 4]) -> [1, 2, 3, 4, 5]
"""

def remove_duplicates(my_list: list) -> list:  # 1 2 5 7 7 8  
    new_list = []
    temp = -1
    my_list.sort()
    for i in range(0, len(my_list)):
        if my_list[i] != temp:
            new_list.append(my_list[i])
            temp = my_list[i]
    return new_list

# print(remove_duplicates([1, 2, 3, 1, 2, 4, 5, 4]))
"""
Exercise-3: Reverse a list
Write a function "reverse_list(my_list: list) -> list" that takes a list of integers and 
returns a new list with the elements in reverse order.

Example:
reverse_list([1, 2, 3, 4, 5]) -> [5, 4, 3, 2, 1]
"""

def reverse_list(my_list: list) -> list:
    my_list.reverse()
    return my_list

# print(reverse_list([1, 2, 3, 4, 5]))

"""
Exercise-4: Find the maximum value in a list
Write a function "max_value(my_list: list) -> int" that takes a 
list of integers and returns the maximum value in the list.

Example:
max_value([1, 2, 3, 4, 5]) -> 5
"""

def max_value(my_list: list) -> int:
    return max(my_list)

# print(max_value([1, 2, 3, 4, 5]))

"""
Exercise-5: Find the minimum value in a list
Write a function "min_value(my_list: list) -> int" that takes a 
list of integers and returns the minimum value in the list.

Example:
min_value([1, 2, 3, 4, 5]) -> 1
"""

def min_value(my_list: list) -> int:
    return min(my_list)

"""
Exercise-6: Sum all values in a list
Write a function "sum_values(my_list: list) -> int" that takes a 
list of integers and returns the sum of all values in the list.

Example:
sum_values([1, 2, 3, 4, 5]) -> 15
"""

def sum_values(my_list: list) -> int:
    sum = 0
    for num in my_list:
        sum += num
    return sum

"""
Exercise-7: Find the average of a list
Write a function "average(my_list: list) -> float" that takes a 
list of integers and returns the average value of the list.

Example:
average([1, 2, 3, 4, 5]) -> 3.0
"""

def average(my_list: list) -> float:
    sum = 0
    for num in my_list:
        sum += num
    return sum / len(my_list)

# print(average([1, 2, 3, 4, 5]))

"""
Exercise-8: Find the index of an element in a list
Write a function "find_index(my_list: list, element: int) -> int" that takes a 
list of integers and an element, and returns the index of the first occurrence of 
the element in the list. If the element is not in the list, return -1.

Example:
find_index([1, 2, 3, 4, 5], 3) -> 2
find_index([1, 2, 3, 4, 5], 6) -> -1
"""

def find_index(my_list: list, element: int) -> int:
    if element in my_list:
        return my_list.index(element)
    return -1

# print(find_index([1, 2, 3, 4, 5], 3))
# print(find_index([1, 2, 3, 4, 5], 6))

"""
Exercise-9: Check if a list is sorted
Write a function "is_sorted(my_list: list) -> bool" that takes a list
of integers and returns True if the list is sorted in non-descending 
order (i.e., each element is greater than or equal to the previous element), 
False otherwise.

Example:
is_sorted([1, 2, 3, 4, 5]) -> True
is_sorted([1, 3, 2, 4, 5]) -> False
"""

def is_sorted(my_list: list) -> bool:
    new_list = sorted(my_list)
    return True if new_list == my_list else False

# print(is_sorted([1, 2, 3, 4, 5]))
# print(is_sorted([1, 3, 2, 4, 5]))
"""
Exercise-10: Count the frequency of an element in a list
Write a function "count_frequency(my_list: list, element: int) -> int" that 
takes a list of integers and an element, and returns the number of 
times the element appears in the list.

Example:
count_frequency([1, 2, 3, 4, 5, 1, 2, 3], 3) -> 2
"""

def count_frequency(my_list: list, element: int) -> int:
    return my_list.count(element)

"""
Exercise-11: Find the mode of a list
Write a function "find_mode(my_list: list) -> int" that takes a list of 
integers and returns the mode (i.e., the value that appears most frequently) 
of the list. If there are multiple modes, return any of them.

Example:
find_mode([1, 2, 3, 4, 5, 1, 2, 2, 3]) -> 2  
"""

def find_mode(my_list: list) -> int: # 1 1 2 2 2 3 3 4 5
    if len(my_list) == 0:
        return None
    
    mode = -1  # store the Mode
    frequency = -1  # Store the mode of most freq number
    my_list.sort()
    temp_freq = 1  # store the frequency of each number
    curr_temp = my_list[0]  # store uniq number
    
    for i in range(1, len(my_list)):
        # first, while we are iterating same number, record the freq
        if my_list[i] == curr_temp:
            temp_freq += 1
            continue
        # If we faced another number, check if prev one is most freq num. And then update our record to prepare for next looking
        if temp_freq > frequency:
            frequency = temp_freq
            mode = my_list[i-1]    
        curr_temp = my_list[i]
        temp_freq = 1

    return my_list[0] if mode == -1 else mode

# print(find_mode([1, 2, 3, 4, 5, 1, 2, 2, 3]))
        
        
            

"""
Exercise-12: Remove all occurrences of an element in a list
Write a function "remove_all(my_list: list, element: int) -> list" 
that takes a list of integers and an element, and returns a new list 
with all occurrences of the element removed.

Example:
remove_all([1, 2, 3, 4, 5, 1, 2, 3], 3) -> [1, 2, 4, 5, 1, 2]
"""

def remove_all(my_list: list, element: int) -> list:
    while element in my_list:
        my_list.remove(element)
    return my_list

# print(remove_all([1, 2, 3, 4, 5, 1, 2, 3], 3))

"""
Exercise-13: Rotate a list to the left by k positions
Write a function "rotate_left(my_list: list, k: int) -> list" that takes a 
list of integers and an integer k, and returns a new list with the elements rotated k positions to the left.

Example:
rotate_left([1, 2, 3, 4, 5], 2) -> [3, 4, 5, 1, 2]
"""

def rotate_left(my_list: list, k: int) -> list:
    new_list = my_list[k:]
    new_list.extend(my_list[:k])
    return new_list

# print(rotate_left([1, 2, 3, 4, 5], 2))

"""
Exercise-14: Rotate a list to the right by k positions
Write a function "rotate_right(my_list: list, k: int) -> list" that 
takes a list of integers and an integer k, and returns a new list 
with the elements rotated k positions to the right.

Example:
rotate_right([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]
"""

def rotate_right(my_list: list, k: int) -> list:
    new_list = my_list[len(my_list)-k:]
    new_list.extend(my_list[:len(my_list)-k])
    return new_list

# print(rotate_right([1, 2, 3, 4, 5], 2))

"""
Exercise-15: Find the intersection of two lists
Write a function "find_intersection(list1: list, list2: list) -> list" that 
takes two lists of integers and returns a new list with the elements that are present in both lists.

Example:
find_intersection([1, 2, 3, 4], [3, 4, 5, 6]) -> [3, 4]
"""

def find_intersection(list1: list, list2: list) -> list:
    l = [num for num in list1 if num in list2]
    return list(set(l))

# print(find_intersection([1, 2, 3, 4], [3, 4, 5, 6]))

"""
Exercise-16: Find the union of two lists
Write a function "find_union(list1: list, list2: list) -> list" that takes 
two lists of integers and returns a new list with the elements that are 
present in either list (i.e., the union of the lists).

Example:
find_union([1, 2, 3, 4], [3, 4, 5, 6]) -> [1, 2, 3, 4, 5, 6]
"""

def find_union(list1: list, list2: list) -> list:
    new_list = list1.copy()
    for num in list2:
        if num not in new_list:
            new_list.append(num)
    return list(set(new_list))

# print(find_union([1, 2, 3, 4], [3, 4, 5, 6]))

"""
Exercise-17: Find the difference of two lists
Write a function "find_difference(list1: list, list2: list) -> list" that takes 
two lists of integers and returns a new list with the elements that are 
present in the first list but not the second list.
Assume that list does not contain duplicates.

Example:
find_difference([1, 2, 3, 4], [3, 4, 5, 6]) -> [1, 2]
"""

def find_difference(list1: list, list2: list) -> list:
    l = [num for num in list1 if num not in list2]
    return l

# print(find_difference([1, 2, 3, 4], [3, 4, 5, 6]))