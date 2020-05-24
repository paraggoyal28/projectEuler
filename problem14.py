if __name__ == "__main__":
    maxi = 0
    number = 0
    for n in range(2, 1000000):
        count = 0
        temp = n
        while(temp!=1):
            if(temp%2==0):
                temp = temp/2
            else: 
                temp = 3 * temp + 1
            count+=1
        if(maxi < count):    
            maxi = max(count, maxi)
            number = n
    print(number)