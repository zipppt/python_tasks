
n = input("введите 8 цифр о 0 до 9: ")
n = int(n)

i = 0
b = 0
a = 0
while n > 0:
    if i > 3:
        b = b + (n%10)
        n = n // 10
    else:
        a = a + (n%10)
        n = n // 10
    i = i + 1
if a == b:
    print('lucky')
else:
    print('No lucky')


print(n)
print(a)
print(b)

