def bubble_sort(arrayToSort):
    a = arrayToSort
    for i in range(len(a),0,-1):
        for j in range(1, i):
            if a[j-1] > a[j]:
                tmp = a[j-1]
                a[j-1] = a[j]
                a[j] = tmp
                print(a)
    return a
ary = [32, 9, 1, 184, 5, 4]
print(bubble_sort(ary))
