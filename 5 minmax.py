def minmax(f):
    max=0
    min=1000 
    for i in range(0, len(f)):
        if f[i]>max:
            max=f[i]
            maxi=i
        if f[i]<min:
            min=f[i]
            mini=i
    f[maxi], f[mini] = f[mini], f[maxi]
    return f

