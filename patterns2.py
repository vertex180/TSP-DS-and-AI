def genPattern(num):
    i = 1
    while (i<=num):
        j = num
        while(j>(i-1)):
            print(' ',end="")
            j = j-1
        print('*' * i,'\n')
        i = i+1

genPattern(6)