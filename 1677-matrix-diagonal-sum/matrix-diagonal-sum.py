class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        r=len(mat)
        c=len(mat[0])
        pd=0
        sd=0
        n=c // 2

        for i in range(r):
            for j in range(c):
                if i==j:
                    pd+=mat[i][j]
        for i in range(r):
            for j in range(c):
                if i+j==c-1:
                    sd+=mat[i][j]
        if c%2==0:
            ans=pd+sd
        else:
            ans=pd+sd-mat[n][n]
        return ans
        
        
                    