def rom_arab(roman):
    numeric = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    arabic = 0
    for d in range(len(roman)):
        try:
            if numeric[roman[d]] < numeric[roman[d + 1]]:
                arabic -= numeric[roman[d]]
            else:
                arabic += numeric[roman[d]]
        except IndexError:
            arabic += numeric[roman[d]]
    return arabic

a = rom_arab('IVX')

print(a)