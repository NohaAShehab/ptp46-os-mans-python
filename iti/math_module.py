

def sum_num(num1 : int, num2 : int) -> int | None:
    if isinstance(num1, int) and isinstance(num2, int):
        return num1 + num2
    print("--- num1 , num2 must be integers ")
    return None

