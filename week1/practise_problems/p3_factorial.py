def fact(n1):
    temp = n1
    res = 1
    if (n1<0):
        print("Invalid Number")
        exit()
    
    while(temp>0):
        res = res*temp
        temp = temp -1
    print(res)


fact(-1)
