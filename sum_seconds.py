a = int(input())
b = int(input())
c = int(input())
sum_of_all = a + b + c
mins = sum_of_all / 60
secs = sum_of_all % 60
print('{0}:{1:02d}'.format(int(mins), secs))
