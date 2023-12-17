import random
from colorama import Fore

num = random.randint(1, 101)


while True:
    try: 
        user_num = int(input("Enter your number: "))
    except Exception as e:
        print("Y")
        continue
    
    if user_num < num:
        print("You ", end="")
        print(Fore.RED + "didn't find it", end="")
        print(Fore.RESET + ". My number was bigger than it!")
    elif user_num > num:
        print("You ", end="")
        print(Fore.RED + "didn't find it", end="")
        print(Fore.RESET + "My number was less than it!")
    else:
        print("You ", end="")
        print(Fore.GREEN + "find it.")
        print(Fore.RESET + "Congratulations")
        break