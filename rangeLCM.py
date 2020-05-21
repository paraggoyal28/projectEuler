def gcd(num, lcm):
    if lcm == 0:
        return num
    else:
        return gcd(lcm, num%lcm)
lcm = 1
for num in range(2, 21):
    lcm = (num * lcm) / gcd(num, lcm)
print(lcm)