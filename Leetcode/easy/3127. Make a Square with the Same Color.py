

class Solution:
    def canMakeSquare(self, grid: list[list]) -> bool:
        # Time: O(1)
        # Space: O(1)
        for r in range(2):
            for c in range(2):
                b = w = 0
                for dr, dc in [(0, 0), (0, 1), (1, 0), (1, 1)]:
                    if grid[r + dr][c + dc] == "B":
                        b += 1
                    else:
                        w += 1
                if b == 3 or w == 3:
                    return True
        return False


