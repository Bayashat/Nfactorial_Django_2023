import requests

api_url = "http://numbersapi.com/"

game = True
            
def continue_gaming() -> bool:
    return 1 if input("Do you want to continue? y/n: ") == "y" else 0



while game:
    choice = int(input("""
                1. MATH
                2. TRIVA
                3. DATE
                4. RANDOM
"""))

    match choice:
        case 1:
            num = int(input("Enter the number: "))
            api_url_math = api_url + "{}/math".format(num)

            res = requests.get(api_url_math)
            print(res.text + "\n")
            
            if continue_gaming():
                continue
            print("Good Bye~")
            game = False
        case 2:
            num = int(input("Enter the number: "))
            api_url_triva = api_url + "{}".format(num)

            res = requests.get(api_url_triva)
            print(res.text + "\n")
            
            if continue_gaming():
                continue
            print("Good Bye~")
            game = False
        case 3:
            dates = input("Enter the date splited by space: ").split(" ")
            api_url_date = api_url + "{}/{}/date".format(dates[0], dates[1])

            res = requests.get(api_url_date)
            print(res.text + "\n")
            
            if continue_gaming():
                continue
            print("Good Bye~")
            game = False
        case _:
            print("\nYou did not enter the correct selection, ReSelect")
            
            
