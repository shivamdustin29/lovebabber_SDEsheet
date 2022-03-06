def rotate(a, n):
    k=a[n-1]
    a.pop(n-1)
    a.insert(0,k)
    
    
    
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
