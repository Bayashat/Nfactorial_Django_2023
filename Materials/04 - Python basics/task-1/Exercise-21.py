"""
 Exercise 21: exponentiation
    Declare a palindrome string (A palindrome is a word that is spelled the same forward and backward. ex: "racecar")
    Check if it is palindromic without using loops
"""

s = "racecar"
if s == s[::-1]:
    print("Its palindeomic")
else:
    print("Its not palindromic")


