from datetime import datetime 

""" 
@author: spanishkukli
@summary: My python utilites.
"""

# Text colors, background and styles classes
class Text():
    BLACK   =    "\33[30m"
    RED     =    "\33[31m"
    GREEN   =    "\33[32m"
    YELLOW  =    "\33[33m"
    BLUE    =    "\33[34m"
    VIOLET  =    "\33[35m"
    BEIGE   =    "\33[36m"
    WHITE   =    "\33[37m"
    GREY    =    "\33[90m"
    RED2    =    "\33[91m"
    GREEN2  =    "\33[92m"
    YELLOW2 =    "\33[93m"
    BLUE2   =    "\33[94m"
    VIOLET2 =    "\33[95m"
    BEIGE2  =    "\33[96m"
    WHITE2  =    "\33[97m"
    
    RESET   =    "\033[39m "


class Background():
    BLACK   =     "\33[40m"
    RED     =     "\33[41m"
    GREEN   =     "\33[42m"
    YELLOW  =     "\33[43m"
    BLUE    =     "\33[44m"
    VIOLET  =     "\33[45m"
    BEIGE   =     "\33[46m"
    WHITE   =     "\33[47m"
    GREY    =     "\33[100m"
    RED2    =     "\33[101m"
    GREEN2  =     "\33[102m"
    YELLOW2 =     "\33[103m"
    BLUE2   =     "\33[104m"
    VIOLET2 =     "\33[105m"
    BEIGE2  =     "\33[106m"
    WHITE2  =     "\33[107m"


class Styles():
    END     =     "\33[0m"
    BOLD    =     "\33[1m"
    ITALIC  =     "\33[3m"
    URL     =     "\33[4m"
    BLINK   =     "\33[5m"
    BLINK2  =     "\33[6m"
    SELECTED =    "\33[7m"


class Status():
    ERROR   =     "\33[31m[ERROR]\033[39m "
    DONE    =     "\33[32m[DONE]\033[39m "
    WARNING =     "\33[33m[WARNING]\033[39m "


text = Text()
bg = Background()
style = Styles()
status = Status()

        
# Execution time decorator
def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        func(*args, **kwargs)
        end_time = datetime.now()
        total_time = (end_time - start_time).total_seconds()
        print("\033[32m" + "[DONE] in {0:.2f} seconds".format(total_time) + "\033[39m")
    
    return wrapper


# Yesno func
def yesno(question, default = "yes"):
    assert default == "yes" or default == "no", "Invalid default parameter, ['yes', 'no']"
    invalid_ans = "\33[33m", "Invalid answer, try again", "\033[39m "
    while True:
        if default == "yes":
            yes = ["yes", "y", ""]
            no = ["no", "n"]
            answer = input(f"{question} [Y/n] (default: yes):").lower()
            if answer in no:
                return False
            elif answer in yes:
                return True
            else:
                print(invalid_ans)
            
        else:
            yes = ["yes", "y"]
            no = ["no", "n", ""]
            answer = input(f"{question} [Y/n] (default: no): ").lower()
            if answer in yes:
                return True
            elif answer in no:
                return False
            else:
                print(invalid_ans)
                




