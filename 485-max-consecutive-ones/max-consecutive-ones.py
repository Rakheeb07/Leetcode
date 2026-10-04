class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        mc=0
        cc=0
        n=len(nums)
        for i in range(n):
            if nums[i] == 1:
                cc+=1
            else:
                mc=max(mc,cc)
                cc=0
        return max(mc,cc)