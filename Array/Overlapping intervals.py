def overlappedInterval(self, Intervals):
        res=[]
        if len(Intervals)==0:
            
            return res
        Intervals.sort()
        temp=Intervals[0]
        for i in  Intervals:
            if(temp[1]>=i[0]):
                
                temp[1]= max(temp[1],i[1])
            else:
                res.append(temp)
                temp= i
                
        res.append(temp)
        return res
#{ 
#  Driver Code Starts
        
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        a = list(map(int, input().strip().split()))
        Intervals = []
        j = 0
        for i in range(n):
            x = a[j]
            j += 1
            y = a[j]
            j += 1
            Intervals.append([x,y])
        obj = Solution()
        ans = obj.overlappedInterval(Intervals)
        for i in ans:
            for j in i:
                print(j, end = " ")
        print()
# } Driver Code Ends
