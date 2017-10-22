def number_as_word(num):
    return{
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
    }.get(num, 'number too big')


num = int(input())
print(number_as_word(num))
