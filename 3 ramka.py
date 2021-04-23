def ramka (a, b):
    '''a это ширина/высота; b это символ'''
    print(b*a)
    if a>1:
        for i in range(1,a-1):
            print(b,b, sep=(' '*(a-2)))
        print(b*a)
