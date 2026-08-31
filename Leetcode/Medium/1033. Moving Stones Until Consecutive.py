

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> list:
        # Time: O(1)
        # Space: O(1)
        a, b, c = sorted([a, b, c])
        if c - a == 2:
            return [0, c - a - 2]
        elif b - a <= 2 or c - b <= 2:
            return [1, c - a - 2]
        return [2, c - a - 2]


