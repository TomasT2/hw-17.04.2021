def aINn (a, n):
    '''a - число, в котором надо найти количество n'''
    k=0
    a=list(str(a))
    for i in range(0, len(a)):
        if a[i]==str(n):
            k+=1
    return k
