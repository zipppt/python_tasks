def QuickSortPos(a, left, right):

    i = left
    j = right - 1
    while (True):#чтобы поставить разделяющий элемент на свое место
        while (a[i] < a[right]): i+=1
        while (a[j] > a[right] and j > left): j-=1
        if (i >= j): break
        a[i],a[j] = a[j],a[i]
    a[right],a[i]  = a[i],a[right]
    print (a)
    return i

ary = [8,2,13,5,44,1]
QuickSortPos(ary, 0, -1)
print (ary)
