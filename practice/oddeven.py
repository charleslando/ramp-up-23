def check_odd_even(number):
    if(number % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(check_odd_even(4))
print(check_odd_even(7))
print(check_odd_even(0))
print(check_odd_even(-5))