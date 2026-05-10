

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # Time: O(n), n = len(moves)
        # Space: O(1)
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")


