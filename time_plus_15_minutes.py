h = int(input())
m = int(input())

time_after = h * 60 + m + 15
hours = int(time_after / 60)
minutes = time_after % 60

if hours >= 24:
    hours = 0

print('{0}:{1:02d}'.format(hours, minutes))
