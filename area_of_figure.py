import math


def area_of_square(a):
    return a * a


def area_of_rectangle(a, b):
    return a * b


def area_of_circle(r):
    return r * r * math.pi


def area_of_triangle(a, h):
    return (a * h) / 2


shape = input()
area = 0
side_a = float(input())
if shape == 'square':
    area += area_of_square(side_a)
elif shape == 'circle':
    area += area_of_circle(side_a)
else:
    side_b = float(input())
    if shape == 'rectangle':
        area += area_of_rectangle(side_a, side_b)
    elif shape == 'triangle':
        area += area_of_triangle(side_a, side_b)
print('{:.3f}'.format(area))
