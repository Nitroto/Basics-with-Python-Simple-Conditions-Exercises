def rates(unit):
    return {
        'm': 1,
        'mm': 1000,
        'cm': 100,
        'mi': .000621371192,
        'in': 39.3700787,
        'km': 0.001,
        'ft': 3.2808399,
        'yd': 1.0936133,
    }.get(unit)


distance = float(input())
from_unit = input()
to_unit = input()
from_unit_to_m = distance * (1 / rates(from_unit))
to_unit_to_m = rates(to_unit)
converted = from_unit_to_m * to_unit_to_m
print('{0} {1}'.format(converted, to_unit))
