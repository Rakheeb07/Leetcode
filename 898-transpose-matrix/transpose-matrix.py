class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m,n=len(matrix),len(matrix[0])
        result=[[0]*m for _ in range(n)]
        for r in range(m):
            for c in range(n):
                result[c][r]=matrix[r][c]
        return result