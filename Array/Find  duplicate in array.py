def duplicates(self, arr, n): 
        # code here
        s=set(arr)
        l=[]
        for i in s:
            a=arr.count(i)
            if a>1:
                l.append(i) 
        if len(l)>0:
            l.sort()
            return l
        else:
            l.append(-1)
            return l
           
            
            

#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()
