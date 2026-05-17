class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        q=[]
        for i in range (len(nums)):
            if(nums[i]==target):
                q.append(i)
            elif(nums[i]>target):
                break
        return q
        