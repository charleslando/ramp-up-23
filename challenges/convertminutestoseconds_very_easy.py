def convert(minutes):
    if type(minutes) != int:
        return "Must input an integer"
    if(minutes < 0):
        return "Must return a positive number"
    return minutes * 60

print(convert(3))
print(convert(5))
print(convert(2))
print(convert("what if I put in a string"))
print(convert(4.8))
print(convert(-7))