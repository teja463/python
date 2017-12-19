def fabinoci(num):
    a = 1
    b = 1
    total = a + b
    if num == 1 or num == 2:
        return 1
    else:
        for i in range(num):
            total = a + b
            a = b
            b = total
        return total - a
    

print (fabinoci(7))
