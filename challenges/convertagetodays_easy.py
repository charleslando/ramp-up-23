def calc_age(age):
    if(type(age) != int):
        return "Must input an integer for the age"
    return age * 365
print(calc_age(10))
print(calc_age(0))
print(calc_age(73))
print(calc_age("what if i give a string"))
print(calc_age(4.6))