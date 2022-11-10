def pythagoreanTriplet(n):
    for i in range(int(n//3), int(n//2)+1):
        for j in range(0, i+1):
            if j**2 + (n-j-i)**2 == i**2:
                print(j, n-j-i, i)
                return i * j * (n-j-i)
    return 0


print(pythagoreanTriplet(12))

print(pythagoreanTriplet(1000))
