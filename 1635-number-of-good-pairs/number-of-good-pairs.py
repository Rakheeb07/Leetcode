class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq={}
        c=0
        for x in nums:
            count=freq.get(x,0)
            c+=count
            freq[x]=count+1
       
        return c