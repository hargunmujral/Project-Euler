def largestPalindromeProd():
    largest = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            prod = i * j
            if prod > largest and str(prod) == str(prod)[::-1]:
                largest = prod
    return largest
print(largestPalindromeProd())