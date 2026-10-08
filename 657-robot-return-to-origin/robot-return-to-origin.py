class Solution:
    
    def judgeCircle(self, moves: str) -> bool:
        # from collections import Counter
        if moves.count("L")==moves.count("R") and moves.count("U")==moves.count("D"):
            return True
        else:
            return False