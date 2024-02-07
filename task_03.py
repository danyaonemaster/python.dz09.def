import re

print("\n\nTask_03\n\n")

user_input = input("Enter a number: ")
function_selection = int(input("Enter a number from 1 to 4 : "))


def calling_functions(function_number, number):
    if function_number == 1:
        return mirror_number(number)
    elif function_number == 2:
        return sum_of_all_numbers(number)
    elif function_number == 3:
        return number_len(number)
    elif function_number == 4:
        return number_squared(number)
    else:
        return "invalid function"


def mirror_number(number):
    return f"mirror number : {number[::-1]}"


def sum_of_all_numbers(number):
    num_list = []
    number_enter = number.replace("", " ")
    number_list = re.split("[. ]", number_enter)
    for num in number_list:
        if num.isnumeric():
            num_list.append(int(num))
    return f"sum number : {sum(num_list)}"


def number_len(number):
    return f"number len : {len(number)}"


def number_squared(number):
    return f"square of the number : {int(number) ** 2}"


print(calling_functions(function_selection, user_input))
