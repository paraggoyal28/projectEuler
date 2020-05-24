#(m+n)/(m)!(n)!
m = 20
n = 20
numWays = 1
for i in range(m+1, m + n + 1):
    numWays *= i
    numWays /= (i-m)
print(numWays )
