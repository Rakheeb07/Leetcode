class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        r=[0]*2*n
        for i in range(n):
            r[i]=nums[i]
            r[i+n]=nums[i]
        return r
