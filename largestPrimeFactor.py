num = 600851475143
i = 2
while  i <= num:
    while (num%i==0):
        num /= i
        maxi = i
    i = i + 1
if (num > 1):
    maxi = max(maxi, num)
print(maxi)
