from collections import Counter
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if len(nums) < 2: return False
        
        m = len(nums) - 1
        
        freq = Counter(nums)
        for i in range(1, m):
            if freq[i] != 1:
                return False
        
        return freq[m] == 2