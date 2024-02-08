import math


def cube(side: float):
    return side ** 3


def cylinder(radius: float, height: float):
    return math.pi * radius ** 2 * height


def sphere(radius: float):
    return (4 / 3) * math.pi * radius ** 3


def pyramid(base_length: float, base_width: float, height: float):
    return (1 / 3) * base_length * base_width * height


def cone(radius: float, height: float):
    return (1 / 3) * math.pi * radius ** 2 * height


def func_switch(function_number: int):
    match function_number:
        case 1:
            side = float(input("\nEnter the length of a square side: "))
            return f"\nThe volume of the cube is: {cube(side)}"

        case 2:
            radius = float(input("\nEnter the radius : "))
            height = float(input("Enter the height : "))
            return f"\nThe volume of the cylinder is: {cylinder(radius, height)}"

        case 3:
            radius = float(input("\nEnter the radius : "))
            return f"\nThe volume of the sphere: {sphere(radius)}"

        case 4:
            base_length = float(input("\nEnter the pyramid base length: "))
            base_width = float(input("Enter the pyramid base width: "))
            height = float(input("Enter the pyramid height: "))
            return f"\nThe volume of the pyramid: {pyramid(base_length, base_width, height)}"

        case 5:
            radius = float(input("\nEnter the radius : "))
            height = float(input("Enter the height : "))
            return f"\nThe volume of the cone: {cone(radius, height)}"
        case _:
            return f"invalid function number: {function_number}"


print("\nTask_04\n")
print("""Enter a function number from 1 to 5 : 
1 - cube volume
2 - cylinder volume
3 - sphere volume
4 - pyramid volume
5 - cone volume
""")
function_selection = int(input())
print(func_switch(function_selection))
