def maxkol():
    '''задаем список. при вводе 0 заканчиваем'''
    f=[]
    while True:
        a=int(input())
        f.append(a)
        if a==0: break
    k=0
    max=0
    for i in range(2, len(f)):
        if i==2 and f[1]==f[i] :k=1
        if f[i]==f[i-1]:
            k=k+1
            if max<k: max=k
        if f[i]!=f[i-1]:
            k=0
    return max+1
