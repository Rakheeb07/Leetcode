class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        r=[True]*n
        r[0]=r[1]=False

        p=2
        while p*p<n:
            if r[2]:
                for i in range(p*p,n,p):
                    r[i]=False
            p+=1
        return sum(r)