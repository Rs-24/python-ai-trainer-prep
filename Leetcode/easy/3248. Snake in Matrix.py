

class Solution:
    def finalPositionOfSnake(self, n: int, commands: list) -> int:
        # Time: O(n)
        # Space: O(1)
        p = 0
        for c in commands:
            p += 1 if c == "RIGHT" else -1 if c == "LEFT" else -n if c == "UP" else n
        return p


