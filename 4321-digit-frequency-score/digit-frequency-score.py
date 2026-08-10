class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        m=str(n)
        freq={}
        for x in m:
            freq[x]=freq.get(x,0)+1
        c=0
        for i in freq:
            a=int(i)*freq[i]
            c+=a
        return c