

class Solution:
    def numMagicSquaresInside(self, grid: list[list]) -> int:
        # Time: O(m * n)
        # Space: O(1)
        m, n = len(grid), len(grid[0])
        def magic(r, c) -> bool:
            if grid[r + 1][c + 1] != 5:
                return False
            s = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if grid[i][j] < 1 or grid[i][j] > 9 or grid[i][j] in s:
                        return False
                    s.add(grid[i][j])
            for i in range(3):
                if sum(grid[r + i][c:c + 3]) != 15:
                    return False
                if grid[r][c + i] + grid[r + 1][c + i] + grid[r + 2][c +  i] != 15:
                    return False
            if grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != 15:
                return False
            if grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != 15:
                return False
            return True
        return sum(magic(r, c) for r in range(m - 2) for c in range(n - 2))


