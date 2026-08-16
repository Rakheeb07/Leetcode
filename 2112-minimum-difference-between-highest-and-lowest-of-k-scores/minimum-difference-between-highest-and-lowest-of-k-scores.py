class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        b=sorted(nums)
        cs=float('inf')
        for i in range(len(b)-k+1):
            c=b[i+k-1]-b[i]
            cs=min(cs,c)
        return cs