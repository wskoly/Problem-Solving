def pageCount(n, p):
    pt=0
    calV=0
    if p%2==0:
        calV = (p*2)+1
    else:
        calV = (p*2)-1
    if  calV<n:
        pt=int(p/2)
    else:
        if n%2 == 0 and p%2 !=0:
            pt = int(((n-p)//2)+1)
        else:
            pt=int((n-p)//2)
    return pt
