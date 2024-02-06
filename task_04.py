import math

print("\n\nTask_04\n\n")

function_selection = int(input("Enter a number from 1 to 5 : "))


def calling_functions(function_number):
    if function_number == 1:
        side = float(input("\nenter the length of the side of the square : "))
        return f"\nVolume of the cube: {calculate_cube_volume(side)}"

    elif function_number == 2:
        radius = float(input("\nenter the radius : "))
        height = float(input("enter the height : "))
        return f"\nVolume of the cylinder: {calculate_cylinder_volume(radius, height)}"

    elif function_number == 3:
        radius = float(input("\nenter the radius : "))
        return f"\nVolume of the sphere: {calculate_sphere_volume(radius)}"

    elif function_number == 4:
        base_length = float(input("\nEnter the base length of the pyramid: "))
        base_width = float(input("Enter the base width of the pyramid: "))
        height = float(input("Enter the height of the pyramid: "))
        return f"\nVolume of the pyramid: {calculate_pyramid_volume(base_length, base_width, height)}"

    elif function_number == 5:
        radius = float(input("\nenter the radius : "))
        height = float(input("enter the height : "))
        return f"\nVolume of the cone: {calculate_cone_volume(radius, height)}"
    else:
        return "invalid function"


def calculate_cube_volume(side):
    return side ** 3


def calculate_cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height


def calculate_sphere_volume(radius):
    return (4 / 3) * math.pi * radius ** 3


def calculate_pyramid_volume(base_length, base_width, height):
    return (1 / 3) * base_length * base_width * height


def calculate_cone_volume(radius, height):
    return (1 / 3) * math.pi * radius ** 2 * height


print(calling_functions(function_selection))
