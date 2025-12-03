class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        w=[]
        q=set(friends)
        for idx in order:
            if idx in q:
                w.append(idx)
        return w