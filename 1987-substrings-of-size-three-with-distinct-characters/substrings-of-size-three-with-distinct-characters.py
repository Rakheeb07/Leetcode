class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        left = 0
        freq = {}
        good = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            if right - left + 1 == 3:
                if len(freq) == 3:
                    good += 1

                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

        return good
