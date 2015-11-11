l = [32, 9, 1, 184, 5, 4]
i = 1

while i < len(l):

    j = 0
    #print(l)
    for j in range(len(l)-i):
        if l[j] > l[j + 1]:

            l[j], l[j + 1] = l[j + 1], l[j]

        print(l)


    i = i + 1

print(l)

