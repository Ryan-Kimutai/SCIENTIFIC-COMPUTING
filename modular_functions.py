import math

def calculate_area(shape, dimension1, dimension2=0):
    if shape == "circle":
        return math.pi * dimension1**2
    elif shape == "rectangle":
        return dimension1 * dimension2
    elif shape == "triangle":
        return 0.5 * dimension1 * dimension2
    else:
        return None

print(calculate_area("circle", 5))
print(calculate_area("rectangle", 4, 6))
print(calculate_area("triangle", 3, 8))
