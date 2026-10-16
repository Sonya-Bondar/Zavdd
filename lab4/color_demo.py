from colorama import init, Fore, Style


def show_color():
    init(autoreset=True)
    print(Fore.GREEN + "Hello, Python!")
    print(Style.BRIGHT + Fore.YELLOW + "Lab 4")