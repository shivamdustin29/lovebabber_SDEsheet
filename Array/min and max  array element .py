def getMinMax( a, n):
    mx=a[0]
    mi=a[0]
    for i in range(len(a)):
        if(a[i]>mx):
            mx=a[i]
        elif(a[i]<mi):
            mi=a[i]
    return [mi,mx]
