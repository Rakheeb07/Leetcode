class Solution:
    def minimumBoxes(self, apple, capacity):
        total = sum(apple)
        capacity.sort(reverse=True)

        boxes = 0
        curr = 0
        
        for c in capacity:
            curr += c
            boxes += 1
            if curr >= total:
                return boxes
