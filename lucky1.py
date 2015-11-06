
n = input("введите 8 цифр о 0 до 9")
n = list(n)

a = (int(n[0]) + int(n[1]) + int(n[2]) + int(n[3]))
b = (int(n[4]) + int(n[5]) + int(n[6]) + int(n[7]))

if a == b:
    print("lucky")
else:
    print("no lucky")

print(n)
print(a)
print(b)

