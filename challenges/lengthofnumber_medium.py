def number_length(num):
    if num < 10:
        return 1
    else:
        return 1 + number_length(num / 10)

assert number_length(10) == 2
assert number_length(5000) == 4
assert number_length(0) == 1
assert number_length(4039182) == 7
assert number_length(9999999999999999) == 16
assert number_length(1) == 1
assert number_length(777777777777777777777777777777) == 30
