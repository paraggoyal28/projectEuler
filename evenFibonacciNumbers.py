a = 1
b = 2
summer = 0
while b <= 4000000:
    if b%2 == 0:
        summer += b
    c = a + b
    a = b
    b = c
print(summer)