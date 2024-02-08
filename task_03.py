import re

print("\n\nTask_03\n\n")


def mirror_number(number):
    return number[::-1]


def sum_of_all_numbers(number):
    num_list = []

    for num in number:
        if num.isnumeric():
            num_list.append(int(num))

    return sum(num_list)


def number_len(number):
    return len(number)


def number_squared(number):
    return int(number) ** 2


def calling_functions(function_number, number):
    match function_number:
        case 1:
            return f"mirror number : {mirror_number(number)}"
        case 2:
            return f"sum number : {sum_of_all_numbers(number)}"
        case 3:
            return f"number len : {number_len(number)}"
        case 4:
            return f"square of the number : {number_squared(number)}"
        case _:
            return "invalid function"


user_input = input("Enter a number: ")
function_selection = int(input("Enter a function number from 1 to 4 : "))

print(calling_functions(function_selection, user_input))
