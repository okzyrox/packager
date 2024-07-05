import colorama
## doesnt actually log anything lmao just for special prints

COLORS = {
    "RED": colorama.Fore.RED,
    "GREEN": colorama.Fore.GREEN,
    "YELLOW": colorama.Fore.YELLOW,
    "BLUE": colorama.Fore.BLUE,
    "CYAN": colorama.Fore.CYAN,
    "MAGENTA": colorama.Fore.MAGENTA,
    "GREY": colorama.Fore.LIGHTBLACK_EX,
    "RESET": colorama.Style.RESET_ALL,
    "WHITE": colorama.Fore.WHITE
}

def output(text, color, indent=0):
    for i in range(0, indent):
        print(" ", end="")
    if not color:
        print(text)
    else:
        print(COLORS[color] + text + COLORS["RESET"])
