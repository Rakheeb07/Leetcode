class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        r = set(nums)
        seen = []
        for i in range(1,len(nums) + 1):
            if i not in r:
                seen.append(i)
        return seen
    
