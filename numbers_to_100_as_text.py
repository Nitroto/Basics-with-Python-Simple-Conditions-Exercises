def get_zero_to_nineteen_as_word(num):
    return {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
    }.get(num)


def get_tenths_as_word(num):
    return {
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety'

    }.get(num)


def transform(num):
    if 0 <= num <= 19:
        return get_zero_to_nineteen_as_word(num)
    elif 20 <= num < 100:
        tenths = int(num / 10)
        units = num % 10

        if units is not 0:
            return '{} {}'.format(get_tenths_as_word(tenths), get_zero_to_nineteen_as_word(units))
        else:
            return get_tenths_as_word(tenths)
    elif num == 100:
        return 'one hundred'
    else:
        return 'invalid number'


number = int(input())
print(transform(number))
