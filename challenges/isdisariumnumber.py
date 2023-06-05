
def is_disarium(n):
    reverse = reverse_num(n)
    final = 0
    counter = 0
    while reverse > 0:
        counter += 1
        final += (reverse % 10) ** counter
        reverse = reverse // 10

    if(n == final):
        return True
    return False

    


def reverse_num(num):
    temp = 0
    while num > 0:
        temp = (temp * 10) + (num % 10)
        num = num // 10
    return temp


print(is_disarium(135))
print(is_disarium(466))
print(is_disarium(518))
