print("Task_01\n\n")


def number_odd_even(num):
    match num % 2 == 0:
        case 1:
            return "is number even"
        case _:
            return "is number odd"


user_input = int(input("Enter a number: "))

print(number_odd_even(user_input))
