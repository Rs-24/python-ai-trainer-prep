# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/robot-return-to-origin/description/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # Time: O(n), n = len(moves)
        # Space: O(1)
        x = y = 0
        for ch in moves:
            if ch == "U":
                y += 1
            elif ch == "D":
                y -= 1
            elif ch == "L":
                x -= 1
            else:
                x += 1
        return x == 0 and y == 0

# One-liner version: 
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # Time: O(n), n = len(moves)
        # Space: O(1)
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")


