class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0 
        left = 0 
        right = len(nums)-1 
        while(left < right):
            if(nums[left] + nums[right] < target): # if nums[left] + nums[right] is less than target
                count += right-left # update the count
                left += 1 # increment the left
            else: 
                right -= 1 
        return count 