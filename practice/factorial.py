def factorial1(num):
    if(num < 0):
        return "Cannot input a negative number"
    if type(num) != int:
        return "Cannot input a non-integer"
    method1 = num
    temp = 1
    while method1 >0:
        temp *= method1
        method1-= 1
    
    return temp

def factorial2(num):
    if(num < 0):
        return "Cannot input a negative number"
    if type(num) != int:
        return "Cannot input a non-integer"
    
    if num <= 1:
        return  1
    else:
        return num * factorial2(num-1)

    
fact = 7
print("Method using loops: ", factorial1(fact))
print("Factorial using recusrion: ", factorial2(fact))




