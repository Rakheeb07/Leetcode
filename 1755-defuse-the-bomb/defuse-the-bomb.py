class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        res=[0]*n
        ws=0

        start = 1 if k>0 else n+k
        end = k if k>0 else n-1

        for i in range(start,end+1):
            ws+=code[i%n]
        for i in range(n):
            res[i]=ws

            ws-=code[start%n]
            ws+=code[(end+1)%n]

            start+=1
            end+=1
            
        return res
