class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        a=set(nums)
        b=len(a)
        if(n!=b):
            return True
        else:
            return False