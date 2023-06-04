def addition(num):
    if type(num) != int:
        return "Must input an integer"
    return num + 1

print(addition(3))
print(addition(5))
print(addition(-2))
print(addition("what if I put in a string"))
print(addition(4.8))
print(addition(-7))