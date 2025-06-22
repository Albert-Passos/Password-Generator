import random
import os

def display():
    os.system("title Password Generator")
    os.system("cls")
    print("----- Password Generator -----\n")
    print(f''' {options[0]} {options[1]} {options[2]} {options[3]} {options[4]} {options[5]} {options[6]}\n\n''')

options = ["[1] \033[31mUppercase (A-Z)\033[0m\n", 
           "[2] \033[31mLowercase (a-z)\033[0m\n", 
           "[3] \033[31mNumbers (0-9)\033[0m\n", 
           "[4] \033[31mSymbols (!@#$%&*)\033[0m\n",
           "[5] \033[31mMarked (á à õ ç ñ ü)\033[0m\n", 
           "[6] \033[31mCyrillic (Д Ж Ф Ю Я)\033[0m\n",  
           "[0] Generate Password"]

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
number = '0123456789'
simbol = r'''`!@#$%^&*()-_=+[]{}|;:'",.<>?/\~``'''
marked = 'ÁáÀàÂâÃãÄäÉéÈèÊêËëÍíÌìÎîÏïÓóÒòÔôÕõÖöÚúÙùÛûÜüÇçÑñÝýŸÿ'
syrilic = 'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя'

selection = ''
password = ''

tog = {
    "upper": False,
    "lower": False,
    "number": False,
    "simbol": False,
    "marked": False,
    "syrilic": False
}

display()

while True:
    option_selected = input("→ ")
    if option_selected.lower() == "0":
            if selection == '':
                print("Select character types (e.g., 1 3 4): ")
            else:
                try:
                    password = ''
                    chars = int(input("Set password length: "))
                    if chars <= 15:
                        display()
                        print("\nFor better security, use more than 15 characters.")
                        for i in range(chars):
                            password += random.choice(selection)
                        print(f"\033[1mPassword:\033[0m {password}")
                    elif chars > 100:
                        display()
                        print("Maximum allowed length is 100 characters.")
                    else:
                        for i in range(chars):
                            password += random.choice(selection)
                        display()
                        print(f"\033[1mPassword:\033[0m {password}")
        
                except:
                    print(f"Error: Password length must be a numeric value.")

    elif option_selected == "1":
        if tog["upper"]:
            selection = selection.replace(upper, "")
            options[0] = "[1] \033[31mUppercase (A-Z)\033[0m\n"
            display()
        else:
            selection += upper
            options[0] = "[1] \033[32mUppercase (A-Z)\033[0m\n"
            display()
            
        tog["upper"] = not tog["upper"]

    elif option_selected == "2":
        if tog["lower"]:
            selection = selection.replace(lower, "")
            options[1] = "[2] \033[31mLowercase (a-z)\033[0m\n"
            display()
        else:
            selection += lower
            options[1] = "[2] \033[32mLowercase (a-z)\033[0m\n"
            display()
        tog["lower"] = not tog["lower"]

    elif option_selected == "3":
        if tog["number"]:
            selection = selection.replace(number, "")
            options[2] = "[3] \033[31mNumbers (0-9)\033[0m\n"
            display()
        else:
            selection += number
            options[2] = "[3] \033[32mNumbers (0-9)\033[0m\n"
            display()
        tog["number"] = not tog["number"]

    elif option_selected == "4":
        if tog["simbol"]:
            selection = selection.replace(simbol, "")
            options[3] = "[4] \033[31mSymbols (!@#$%&*)\033[0m\n"
            display()
        else:
            selection += simbol
            options[3] = "[4] \033[32mSymbols (!@#$%&*)\033[0m\n"
            display()
        tog["simbol"] = not tog["simbol"]

    elif option_selected == "5":
        if tog["marked"]:
            selection = selection.replace(marked, "")
            options[4] = "[5] \033[31mMarked (á à õ ç ñ ü)\033[0m\n"
            display()
        else:
            selection += marked
            options[4] = "[5] \033[32mMarked (á à õ ç ñ ü)\033[0m\n"
            display()
        tog["marked"] = not tog["marked"]

    elif option_selected == "6":
        if tog["syrilic"]:
            selection = selection.replace(syrilic, "")
            options[5] = "[6] \033[31mCyrillic (Д Ж Ф Ю Я)\033[0m\n"
            display()
        else:
            selection += syrilic
            options[5] = "[6] \033[32mCyrillic (Д Ж Ф Ю Я)\033[0m\n"
            display()
        tog["syrilic"] = not tog["syrilic"]

    else:
        print("Error: Option not recognized.")
