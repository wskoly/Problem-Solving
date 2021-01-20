def arrayManipulation(n, queries):
    arr = [0] * (n+1)
    for i in queries:
        arr[(i[0]-1)] += i[2]
        arr[(i[1])] -= i[2]
    
    maxi = 0
    prev = 0
    for i in arr:
        prev += i
        if prev>maxi:
            maxi = prev   
    return maxi
