def a(ary):
    l = ary
    i = 0
    temp = None
    while i < len(l) - 1:
        if l[i] > l[i + 1]:
            temp = l[i]
            l[i] = l[i + 1]
            l[i + 1] = temp
            i = 0
        else:
            print(l)
            i = i + 1
    return l
ary = [32, 9, 1, 184, 5, 4]
print(a(ary))

