def search(arr,n,x):
  if x not in arr:
        return [-1,-1]
    d = arr.index(x)
    k = d
    for i in range(d,n):
        if arr[i] == x:
            k = i
    return [d,k]
