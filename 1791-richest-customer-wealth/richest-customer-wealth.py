class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ms=0
        for i in accounts:
            ms=max(sum(i),ms)

        return ms



