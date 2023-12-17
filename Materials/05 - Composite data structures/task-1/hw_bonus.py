"""
💎 Exercise-1 (Longest Consecutive Sequence):
Write a function "longest_consecutive(my_list: list[int]) -> int" that takes a 
list of integers and returns the length of the longest consecutive elements 
sequence in the list. The list might be unsorted.

Example:

longest_consecutive([100, 4, 200, 1, 3, 2]) -> 4
"""


def longest_consecutive(my_list: list[int]) -> int:  # 1 5 7 8 9 10 11 12  
    cnt = 0
    my_list.sort()
    temp = 0
    for i in range(len(my_list)):
        if my_list[i] == temp+1:
            cnt += 1
            temp = my_list[i]
    return cnt

# print(longest_consecutive([1, 2, 2, 2, 3]))
# print(longest_consecutive([1,5,7,8,9,10,11,12]))
# print(longest_consecutive([100,4,200,1,3,2]))
# print(longest_consecutive([1, 2, 3, 4, 5, 7,8,9,10,11, 12]))


"""
💎 Exercise-2 (Find missing number):
Write a function "find_missing(my_list: list[int]) -> int" that takes a 
list of integers from 1 to n. The list can be unsorted and have one 
number missing. The function should return the missing number.

Example:

find_missing([1, 2, 4]) -> 3
"""


def find_missing(my_list: list[int]) -> int:
    my_list.sort()
    for i in range(1, len(my_list)+1):
        if i != my_list[i-1]:
            return i
    return None

# print(find_missing([1, 2, 4]))
# print(find_missing([1]))


"""
💎 Exercise-3 (Find duplicate number):
Write a function "find_duplicate(my_list: list[int]) -> int" that takes a list 
of integers where each integer is in the range of 1 to n (n is the size of the list). 
The list can have one number appearing twice and the function should return this number.

Example:

find_duplicate([1, 3, 4, 2, 2]) -> 2
"""


def find_duplicate(my_list: list[int]) -> int:
    my_list.sort()
    for i in range(1, len(my_list)+1):
        if i != my_list[i-1]:
            return my_list[i-1]


# print(find_duplicate([1, 3, 4, 2, 2])) # 1 2 2 3 4
# print(find_duplicate([3, 1, 3, 4, 2]))  # 1 2 3 3 4
# print(find_duplicate([1, 1]))


"""
💎 Exercise-4 (Group Anagrams):
Write a function "group_anagrams(words: list[str]) -> list[list[str]]" that 
takes a list of strings (all lowercase letters), groups the anagrams together, 
and returns a list of lists of grouped anagrams.

An Anagram is a word or phrase formed by rearranging the letters of 
a different word or phrase, typically using all the original letters exactly once.

group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) 
-> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
"""


def group_anagrams(words: list[str]) -> list[list[str]]:
    anagram_groups = {}

    for word in words:
        # Sort the characters of the word and use it as a key in the dictionary
        sorted_word = ''.join(sorted(word))
        # print(sorted_word)
        
        # If the key is not in the dictionary, create a new list
        if sorted_word not in anagram_groups:
            anagram_groups[sorted_word] = [word]
        else:
            # If the key is already in the dictionary, append the word to the list
            anagram_groups[sorted_word].append(word)

    # Convert the dictionary values to a list of lists
    result = list(anagram_groups.values())

    return result

# # Example usage:
# result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
# print(result)