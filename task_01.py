print("Task_01\n\n")

user_input = int(input("Enter a number: "))


def number_odd_even(n):
    if n % 2 == 0:
        print("is number even")
    else:
        print("is number odd")


number_odd_even(user_input)