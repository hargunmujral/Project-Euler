def multOf3Or5():
    return sum([a for a in range(1000) if a % 3 == 0 or a % 5 == 0])

print(multOf3Or5())
