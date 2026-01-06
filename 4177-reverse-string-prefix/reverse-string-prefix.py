class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        arr = list(s)
        l = 0
        r = k - 1

        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

        return "".join(arr)
