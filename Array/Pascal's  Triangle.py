class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for row in range(numRows):
            add = []
            for i in range(row+1):
                if row == i or 0 == i:
                    add.append(1)
                else:
                    add.append(triangle[row-1][i-1] + triangle[row-1][i])
            triangle.append(add)
        return triangle
        
