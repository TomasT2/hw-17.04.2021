def join(a, r):
    '''а - список, r - разделитель'''
    m=''
    for i in range(0, len(a)):
        m=str(m)+str(a[i])+str(r)
    return m

