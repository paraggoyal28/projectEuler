num = (2 ** 1000)
print(num)
sumDigits = 0
while(num>0):
    sumDigits += num%10
    num = num //10 
print(sumDigits)