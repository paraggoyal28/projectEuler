def isPrime(n):
    i = 2
    while (i * i  <= n):
        if n%i == 0:
            return False
        i = i + 1
    return True 


if __name__ == "__main__":
    summation = 0
    for i in range(2, 2000000):
        if isPrime(i):
            summation += i
    print(summation)