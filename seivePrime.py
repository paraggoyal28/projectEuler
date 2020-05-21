def isPrime(num):
    i = 2
    while i * i <= num:
        if (num % i == 0):
            return False
        i = i + 1
    if num > 1:
        return True
    return False

if __name__=="__main__":
    n = 1000000
    count = 0
    for i in range(2, n+1):
        if(isPrime(i)):
            count= count+1
            if(count==10001):
                print(i)
                break