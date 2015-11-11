
m = input("введите сколько хотите цифр о 0 до 9: ")
m = int(m)
n = m
i = 1
b = 0
a = 0
j = 1
while m > 0:
    m = m // 10
    if m == 0:
        s = j%2
        k = j/2
        if s == 0:
            while n > 0:
                if k < i:
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
        else:
            k = s + j // 2
            while n > 0:
                if k == i:
                    c = (n%10)
                    n = n // 10
                elif k > i:
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
    else:
        j = j + 1
print(n)
print(a)
print(b)
print(m)
print(i)
print(j)
