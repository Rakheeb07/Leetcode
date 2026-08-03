class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m=len(accounts)
        n=len(accounts[0])
        ms=0
        
        for i in range(m):
            s=0
            for j in range(n):
                
                s+=accounts[i][j]
            ms=max(ms,s)
        return ms


