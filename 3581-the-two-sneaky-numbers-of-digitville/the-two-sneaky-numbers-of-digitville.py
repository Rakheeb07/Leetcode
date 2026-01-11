class Solution:
    def getSneakyNumbers(self, a: List[int]) -> List[int]:
        q = set()
        return [v for v in a if v in q or q.add(v)]