num = int(input())
even_bonus = 1 if num % 2 == 0 else 0
finish_on_five_bonus = 2 if str(num)[-1] == '5' else 0
bonus = even_bonus + finish_on_five_bonus
if num <= 100:
    bonus += 5
elif num <= 1000:
    bonus += 0.2 * num
else:
    bonus += 0.1 * num
print(bonus)
print(num + bonus)
