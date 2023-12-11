"""
 Exercise 22: check-anagrams
    Declare 2 strings
    Check if the strings are anagrams (ignoring case)
    Print the result
    
    *Anagram - a word, phrase, or name formed by rearranging the letters of another, such as spar, formed from rasp.
"""
a = "rasp"
b = "spar"

if sorted(a) == sorted(b):
    print("They are Anagram")
else:
    print("They are not Anagram")