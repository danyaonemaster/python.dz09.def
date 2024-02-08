import re


def mirror_str(input_str: str):
    return input_str[::-1]


def sum_all(input_str: str):
    return sum(int(i) for i in input_str if i.isnumeric())


def my_len(input_str: str):
    return len(input_str)


def square(input_str: str):
    return int(input_str) ** 2


def func_switch(function_number, input_value):
    match function_number:
        case 1:
            return f"mirrored number is: {mirror_str(input_value)}"
        case 2:
            return f"sum of numbers digits is : {sum_all(input_value)}"
        case 3:
            return f"input len is: {my_len(input_value)}"
        case 4:
            return f"square of the number is: {square(input_value)}"
        case _:
            return f"invalid function number : {function_number}"


print("\nTask_03\n")

user_input = input("Enter a number: ")
print('''Enter a function number from 1 to 4 :
1 - marrow input
2 - sum all input digits
3 - input len
4 - square number
''')
function_selection = int(input())

print(func_switch(function_selection, user_input))
