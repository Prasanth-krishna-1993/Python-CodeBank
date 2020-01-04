def factorialOfNumber(n):
    flag = 1
    while (n != 0):
        flag = flag * n
        n -= 1

    return flag
    
