ticket = input("input ticket: ")
ticket = int(ticket)

count = 0
while True:
    count += 1
    if ticket // (10 ** count) > 0:
        continue
    break

if count == 1:
    print("not lucky")
else:
    group = count // 2
    even = group == count / 2.0

    sum_l = 0
    sum_r = 0

    i = 0
    while ticket > 0:
        i += 1
        n = ticket % 10
        ticket //= 10

        if not even and i == group + 1:
            continue

        if i <= group:
            sum_r += n
        else:
            sum_l += n

    if sum_r == sum_l:
        print("lucky")
    else:
        print("not lucky")



