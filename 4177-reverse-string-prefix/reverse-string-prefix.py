class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        a=list(s)
        l=0
        r=k-1
        while l<r:
           a[l],a[r]=a[r],a[l]
           l+=1
           r-=1
        return "".join(a)