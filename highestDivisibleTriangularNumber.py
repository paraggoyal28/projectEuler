def divisorCount(num):
    i = 1
    countDivisors = 0
    while i * i <= num:
        if(num % i == 0):
            countDivisors += 1
        i += 1
    return 2 * countDivisors

if __name__ == "__main__":
    n = 7
    m = (n * (n+1))/2
    while divisorCount(m) <= 500:
        n += 1
        m = (n*(n+1))/2
    print(m)
    
