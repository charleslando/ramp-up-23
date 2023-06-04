def sum_odd_and_even(lst):
    odds = 0
    evens = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            evens += lst[i]
        else:
            odds += lst[i]

    return [evens, odds]

print(sum_odd_and_even([1, 2, 3, 4, 5, 6]))
print(sum_odd_and_even([12,9]))
print(sum_odd_and_even([-1, -2, -3, -4, -5, -6]))
print(sum_odd_and_even([0, 0]))
