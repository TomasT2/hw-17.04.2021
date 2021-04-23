def plusodin(f):
    g=f[-1]
    for i in range(len(f)-1, 0, -1):
        f[i]=f[i-1]
    f[0]=g
    return(f)
