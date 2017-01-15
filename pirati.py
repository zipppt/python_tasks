a, m = map(int, input().split())

n = 0
# a = c
z = 0
c = 0


while z < m:
    # z = ((a + n + 1) * 2) + a
    c = c + a + n
    z = (a+n+1) * 2 + c
    n +=1
print(n)
    # print(z)



print(n+1)
