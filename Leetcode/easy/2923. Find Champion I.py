

class Solution:
    def findChampion(self, grid: list[list]) -> int:
        # Time: O(n^2)
        # Space: O(1)
        n = len(grid)
        for c in range(n):
            champion = True
            for r in range(n):
                if r != c and grid[r][c] == 1:
                    champion = False
                    break
            if champion:
                return c


