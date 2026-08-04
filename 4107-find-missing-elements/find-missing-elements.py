class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        m=max(nums)
        q=min(nums)
        r=[]
        for i in range(q,m+1):
            if i not in nums:
                r.append(i)
        return r




