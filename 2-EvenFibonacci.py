def evenFib(n):
    ptr1 = 1
    ptr2 = 1
    sum = 0
    while ptr2 <= n:
        ptr1, ptr2 = ptr2, ptr2+ptr1
        sum += ptr2 if ptr2 % 2 == 0 else 0
    return sum


print(evenFib(4 * 10 ** 6))
