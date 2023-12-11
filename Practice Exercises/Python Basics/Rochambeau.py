import random
from colorama import Fore

def convert_choice(choice: int) -> str:
    # print(choice)
    if choice == 1:
        return "Stone"
    elif choice == 2:
        return "Scissors"
    else:
        return "Paper"

def get_input(user_input: int):
    if user_input in [1,2,3]:
        return user_input
    raise Exception

def gaming(user, computer):
    if (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1):
        print(Fore.GREEN + "Congratulations, You Win 🤩\n" + Fore.RESET)
    elif user == computer:
        print(Fore.YELLOW + "Tie\n" + Fore.RESET) 
    else:
        print(Fore.RED + "You a Loser 😂\n" + Fore.RESET)
    
    print(f"Your choice was '{convert_choice(user)}'\nComputer's was '{convert_choice(computer)}'\n")


def main():
    continue_game = True

    print("Welcome to the Game~~~\n")
    while continue_game:
        computer = random.randint(1, 3)  
        try:
            user = get_input(int(input("What's your Choice?\n 1 => Stone\n 2 => Scissors\n 3 => Paper\n")))
        except Exception:
            print("Invalid Input, try agian! 😡\n")
            continue

        gaming(user, computer)
            
        continue_game = True if input("Do you want to continue?\n y/n\n") == 'y' else False


main()