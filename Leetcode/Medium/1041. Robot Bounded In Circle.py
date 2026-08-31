

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # Time: O(n)
        # Space: O(1)
        t = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x = y = 0
        d = 0
        for p in instructions:
            if p == "G":
                x += t[d][0]
                y += t[d][1]
            elif p == "L":
                d = (d - 1) % 4
            else:
                d = (d + 1) % 4
        return (x == y == 0) or d != 0


