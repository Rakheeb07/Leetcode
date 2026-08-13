class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
       c=0
       freq={}
       for x in nums:
        c+=freq.get(x-k,0)
        c+=freq.get(x+k,0)
        freq[x]=freq.get(x,0)+1
       return c 