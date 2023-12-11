import random

def generate_show_word(word):
    return "_" * len(word)

def show_words(word, show_word, user_letter):
    for i in range(len(word)):
        if word[i] == user_letter:
            show_word = show_word[:i] + user_letter + show_word[i+1:]
            # print(show_word, i, show_word[i], user_letter)
    return show_word
    
def check_input(input, attempts):
    checked = True
    if len(input) > 1:
        attempts -= 1
        print(f"Only 1 characters one time. Try again! You have {attempts} attempts")
        checked = False
    elif not input.isalpha():
        attempts -= 1
        print(f"Try again, you have {attempts} attempts")
        checked = False
    return checked, attempts

def guess_word(word, show_word: str, attempts):
    print("I thought of a word")
    while True:
        if attempts == 0:
            print(f"\nYou are loser, the word was '{word}'")
            break
        
        user_letter = input("Enter a letter: ")
        
        checked, attempts = check_input(user_letter, attempts)
        if checked:
            if user_letter in word:
                show_word = show_words(word, show_word, user_letter)
                print(show_word)
                if '_' not in show_word:
                    print("Congratulation, you did it!!!")
                    break
            else:
                attempts -= 1
                print(f"Try again, you have {attempts} attempts")

def main():
    word = "nFactorial"
    attempts = len(word) * 2
    
    show_word = generate_show_word(word)
    
    guess_word(word, show_word, attempts)
    
main()
    