

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list) -> int:
        # Time: O(n^2)
        # Space: O(n)
        r = [max(x) for x in grid]
        c = [max(y) for y in zip(*grid)]
        a = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                a += min(r[i], c[j]) - grid[i][j]
        return a


