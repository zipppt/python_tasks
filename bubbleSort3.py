def bubbleSort(a):
    for passnum in range(len(a)-1,0,-1):
        print(a)
        for i in range(passnum):
            if a[i]>a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
                print(a)

a = [32, 9, 1, 184, 5, 4]
bubbleSort(a)
print(a)

