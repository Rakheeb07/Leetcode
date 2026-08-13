class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(int("".join(reversed(str(n)))) - n)