def gen_sum(n, s, base=10, startwith=None):
    startwith = startwith or []
    start = int(startwith[0]) if len(startwith) > 0 else -1
    if n == 1:
        if s < base:
            yield str(s)
    else:
        for i in range(max(0, start, s - (n - 1) * (base - 1)), min(s, base - 1) + 1):
            for sub in gen_sum(n - 1, s - i, base, startwith[1:] if i == start else None):
                yield str(i) + sub

def gen_lucky(n=3, base=10, startwith=None):
    startwith = startwith or []
    startsum = sum(map(int, startwith[0:n]))
    for s in range(max(0, startsum), n * (base - 1) + 1):
        for lucky1 in gen_sum(n, s, base, startwith[0:n]):
            for lucky2 in gen_sum(n, s, base, startwith[n:n*2] if lucky1 == startwith[0:n] else None):
                yield lucky1 + lucky2

for i in gen_lucky(startwith='555564'):
    print(i)
