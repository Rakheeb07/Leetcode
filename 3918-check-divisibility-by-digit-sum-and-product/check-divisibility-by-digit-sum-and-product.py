class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = sum(int(d) for d in str(n))
        p = 1
        for d in str(n):
            p *= int(d)
        
        return n % (s + p) == 0

