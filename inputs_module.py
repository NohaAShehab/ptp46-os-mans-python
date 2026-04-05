
print("-------------------------")
def ask_for_int(prompt :str  = 'Please enter an integer:') -> int:
    while True:
        num = input(f"{prompt}")
        if num.isdigit():
            return int(num)
        print("----- please enter valid integer -----")


def ask_for_string(prompt :str = 'Please enter a string:') -> str:
    while True:
        anystring = input(f"{prompt}")
        if anystring.isalpha():
            return anystring
        print("----- please enter valid string -----")



# limit when to run  these lines ?? I need to run them ?
# when inputs modules is the starting point of run
# if __name__ == "__main__":
print("**************Welcome to inputs module ***********************")
print(ask_for_int(prompt="Please enter an integer: "))