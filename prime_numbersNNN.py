limit = input("input limit: ")
limit = int(limit)

prime_numbers = list()
excluded_numbers = list()


n = 2
while n <= limit:
    prime_numbers.append(n)
    m = n + 1
    while m <= limit:
        while m in excluded_numbers:
            m += 1
            continue

        if m % n == 0:
            excluded_numbers.append(m)

        m += 1

    n += 1
    while n in excluded_numbers:
        n += 1

print(prime_numbers)