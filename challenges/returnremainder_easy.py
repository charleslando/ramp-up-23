def remainder(x, y):
    if type(x) != int:
        return "First number must be an integer"
    if type(y) != int:
        return "Second number must be an integer"
    return x % y
print(remainder(1, 3))

print(remainder(3, 4))

print(remainder(5, 5))

print(remainder(7, 2))