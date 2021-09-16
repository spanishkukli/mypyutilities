from datetime import datetime

def text_color():
    return ["\33[30m",
            "\33[31m",
            "\33[32m",
            "\33[33m",
            "\33[34m",
            "\33[35m",
            "\33[36m",
            "\33[37m",
            "\033[39m "]

BLACK, RED, GREEN, YELLOW, BLUE, VIOLET, BEIGE, WHITE, RESET = text_color()

def text_color2():
    return ["\33[90m",
            "\33[91m",
            "\33[92m",
            "\33[93m",
            "\33[94m",
            "\33[95m",
            "\33[96m",
            "\33[97m"]

GREY, RED2, GREEN2, YELLOW2, BLUE2, VIOLET2, BEIGE2, WHITE2 = text_color2()

def text_style():
    return ["\33[0m",
            "\33[1m",
            "\33[3m",
            "\33[4m",
            "\33[5m",
            "\33[6m",
            "\33[7m"]
    
END, BOLD, ITALIC, URL, BLINK, BLINK2, SELECTED = text_style()
    
def bg_color():
    return ["\33[40m",
            "\33[41m",
            "\33[42m",
            "\33[43m",
            "\33[44m",
            "\33[45m",
            "\33[46m",
            "\33[47m"]
    
BLACKBG, REDBG, GREENBG, YELLOWBG, BLUEBG, VIOLETBG, BEIGEBG, WHITEBG = bg_color()

def bg_color2():
    return ["\33[100m",
            "\33[101m",
            "\33[102m",
            "\33[103m",
            "\33[104m",
            "\33[105m",
            "\33[106m",
            "\33[107m"]

GREYBG, REDBG2, GREENBG2, YELLOWBG2, BLUEBG2, VIOLETBG2, BEIGEBG2, WHITEBG2 = bg_color2()


def status_colors():
    return [RED + "[ERROR]" + RESET, 
            GREEN + "[DONE]" + RESET,
            YELLOW + "[WARNING]" + RESET]
    
ERROR, DONE, WARNING = status_colors()

# Execution time decorator
def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        func(*args, **kwargs)
        end_time = datetime.now()
        total_time = (end_time - start_time).total_seconds()
        print("\033[32m" + "[DONE] in {0:.2f} seconds".format(total_time) + "\033[39m")
    
    return wrapper


def yesno(question, default = "yes"):
    assert default == None or default == "yes" or default == "no", "Invalid default parameter, [None, 'yes', 'no']"
    while True:
        if default == "yes":
            yes = ["yes", "y", ""]
            no = ["no", "n"]
            answer = input(f"{question} [Y/n] (default: yes):").lower()
            print(answer)
            if answer in no:
                return False
            elif answer in yes:
                return True
            else:
                print("invalid val")
            
        else:
            yes = ["yes", "y"]
            no = ["no", "n", ""]
            answer = input(f"{question} [Y/n] (default: no): ").lower()
            if answer in yes:
                return True
            elif answer in no:
                return False
            else:
                print("invalid val")
            
        