import math
for a in range(0, 999):
    for b in range(0, 999):
        c = math.sqrt(a**2 + b**2)
        if c + a + b == 1000:
            print(a* b * c)
            print(a, b, c)
            break
