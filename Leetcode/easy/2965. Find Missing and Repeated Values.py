

class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list]) -> list:
        # Time: O(n^2)
        # Space: O(n^2)
        n = len(grid)
        count = [0] * (n**2)
        for r in range(n):
            for c in range(n):
                count[grid[r][c] - 1] += 1
        r = m = -1
        for i, c in enumerate(count):
            if c == 0:
                m = i + 1
            elif c == 2:
                r = i + 1
        return [r, m]


