maxi = 0
for firstNum in range(100, 999):
    for secondNum in range(100, 999):
        res =  firstNum * secondNum
        temp = str(res)
        if(temp == temp[::-1]):
            maxi = max(maxi, res)
print(maxi)        
