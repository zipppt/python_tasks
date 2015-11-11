a = [32, 9, 1, 184, 5, 4]

for i in range(len(a)):
    v = a[i]
    j = i
    while (a[j-1] > v) and (j > 0):
        a[j] = a[j-1]
        j -= 1
    a[j] = v
    print(a)
