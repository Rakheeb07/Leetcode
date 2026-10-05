class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        last_fruit = -1
        second_last_fruit = -1
        last_count = 0
        curr_max = 0
        max_len = 0
        
        for fruit in fruits:
            if fruit == last_fruit or fruit == second_last_fruit:
                curr_max += 1
            else:
                curr_max = last_count + 1
                
            if fruit == last_fruit:
                last_count += 1
            else:
                last_count = 1
                second_last_fruit = last_fruit
                last_fruit = fruit
                
            max_len = max(max_len, curr_max)
            
        return max_len