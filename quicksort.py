def quicksort(a, l, r):
    if (r > l):
        v = a[r]
        i = l - 1
        j = r
        #partition
        while (True):
            i = i + 1
            j = j - 1
            while(a[i] < v):
                i = i + 1
            while(a[j] > v):
                j = j - 1
            if (i >= j):
                break;
            t = a[i]
            a[i] = a[j]
            a[j] = t
        t = a[i]
        a[i] = a[r]
        a[r] = t
        #next sort
        quicksort(a, l, i - 1)
        quicksort(a, i + 1, r)

ary = [8,2,13,5,44,1]
quicksort(ary, 0, len(ary)-1)
print (ary)
