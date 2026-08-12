class Solution:
    def maxSum(self, nums: List[int]) -> int:
        mv=[-1]*10
        ans=-1
        for x in nums:
            md=max(int(d) for d in str(x))

            if mv[md]!=-1:
                ans=max(ans,x+mv[md])
            mv[md]=max(mv[md],x)
        return ans