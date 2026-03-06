class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        r = list(s)
        l = 0

        for i in range(1, len(r)):
            if r[i] == '1' and r[i-1] == '0':
                return False

        return True