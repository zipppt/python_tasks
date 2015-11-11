l = [32, 9, 1, 184, 5, 4]

i = 0
temp = None
while i < len(l) - 1:
    j = 0
    while j < len(l) - 1:
        if l[j] > l[j + 1]:
            temp = l[j]
            l[j] = l[j + 1]
            l[j + 1] = temp
            print(l)
        j = j + 1
    i = i + 1

print(l)
