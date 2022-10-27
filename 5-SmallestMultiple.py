def smallestMultiple(n):
    output = 1
    for i in range(2, n):
        if output % i != 0:
            for j in range(1, n):
                if (output * j) % i == 0:
                    output *= j
                    break
    return output

print(smallestMultiple(20))
