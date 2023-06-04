def reverse(string):
    reverse = string[::-1]
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in range(len(string)):
        if string[i] in vowels:
            count += 1

    return reverse, count

print(reverse("Hello World!"))
print(reverse("My name is Charles Lando"))