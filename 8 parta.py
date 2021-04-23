def parta(a,b,c):
    '''a- кол-во парт в первом классе, b во втором, с в третьем'''
    if a%2!=0: a=(a//2)+1
    else: a=a//2
    if b%2!=0: b=(b/2)+1
    else: b=b//2
    if c%2!=0: c=(c//2)+1
    else: c=c//2
    return a+b+c
