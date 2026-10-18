class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        c=0
        for i in range(len(patterns)):
            if patterns[i] in word:
                c+=1
        return c
