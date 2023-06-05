def sock_merchant(lst):
    pairs = 0
    for i in range(len(lst)):
        temp = lst[:i] + lst[i+1:]
        if lst[i] in temp:
            pairs += 1
    return pairs//2

print(sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]))
print(sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90]))
print(sock_merchant([]))

