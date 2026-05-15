

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> list[list[int]]:
        # Time: O(rows * cols log (rows * cols))
        # Space: O(rows * cols)
        cells = []
        for r in range(rows):
            for c in range(cols):
                cells.append((abs(r - rCenter) + abs(c - cCenter), r, c))
        cells.sort()
        return [[r, c] for _, r, c in cells]


