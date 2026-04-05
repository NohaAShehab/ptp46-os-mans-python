# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#
# temp  = 'We are {no_stds} in OS track'
# print(temp.format(no_stds=30))

def sum_num():
    try:
        num1 = int(input("please enter num1: "))
        num2 = int(input("please enter num2: "))
        res = num1 / num2
    except Exception as  e:
        print(e)
        res = math.nan
        return res
    else:
        print(res)
        return res

    finally:
        # execution of finally preceeds return
        print("=== Marked safe from this function ===")
    print("***************************************************")


print(sum_num())
