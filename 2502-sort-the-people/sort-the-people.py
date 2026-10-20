class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        paired = zip(heights, names)
        sorted_pairs = sorted(paired, reverse=True)
        return [name for height, name in sorted_pairs]