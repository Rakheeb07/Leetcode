class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        q=[]
        w=[]
        for i in range(1,n+1):
            if(i%m==0):
                w.append(i)
            else:
                q.append(i)
        r=sum(q)-sum(w)
        return r