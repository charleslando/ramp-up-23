def reverse_num(num):
    temp = 0
    while num > 0:
        temp = num/10
        temp*=10
    return temp

#def is_disarium(n):



print(reverse_num(78126))
print(reverse_num(7))
print("hi")