class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        c=0
        l=0
        r=sum(nums)
        for i in range(len(nums)-1):
            l=l+nums[i]
            r=r-nums[i]
            if(l-r)%2==0:
                c=c+1
        return c