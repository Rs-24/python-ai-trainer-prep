

class Solution:
    def reverseSubmatrix(self, grid: list[list], x: int, y: int, k: int) -> list[list]:
        # Time: O(n^2)
        # Space: O(1)
        r = x
        b = x + k - 1
        while r < b:
            for c in range(y, y + k):
                grid[r][c], grid[b][c] = grid[b][c], grid[r][c]
            r += 1
            b -= 1
        return grid 


