class Solution:
    def countTriples(self, n: int) -> int:
        c = 0
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                ksq = i*i + j*j
                k = int(ksq**0.5)
                if k <= n and k*k == ksq:
                    c += 1
        return c*2
