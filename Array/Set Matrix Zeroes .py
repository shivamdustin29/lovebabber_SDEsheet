class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n,m=len(matrix),len(matrix[0])
        col,row=False,False
        
    #check if first row and col has zero 
    
        for i in range(n):
            if matrix[i][0]==0:col=True
        for i in range(m):
            if matrix[0][i]==0:row=True
                
    #if position has zero set first col and first row zero for that 
    
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j]==0:
                    matrix[0][j]=matrix[i][0]=0
                    
    #for every zero in first col set zero for every postion on that row
    
        for i in range(1,n):
            if matrix[i][0]==0:
                for j in range(1,m):
                    matrix[i][j]=0
                
    #for every zero in first row set zero for every postion on that col
    
        for j in range(1,m):
            if matrix[0][j]==0:
                for i in range(1,n):
                     matrix[i][j]=0
                        
    # if any of the check is true change all postions to zero

        if col:
            for i in range(n):
                matrix[i][0]=0

        if row:
            for j in range(m):
                matrix[0][j]=0
     
        
