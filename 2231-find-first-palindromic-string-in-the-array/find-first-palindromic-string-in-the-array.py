class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            l = 0
            r = len(word) - 1
            is_pal = True

            while l < r:
                if word[l] != word[r]:
                    is_pal = False
                    break
                l += 1
                r -= 1

            if is_pal:
                return word

        return ""
