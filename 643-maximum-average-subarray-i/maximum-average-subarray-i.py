class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        s=0
        for i in range(k):
            s += nums[i]
        ms=s
        for i in range(k,n):
            s =s-nums[i-k]+nums[i]
            ms=max(ms,s)
        return ms/k