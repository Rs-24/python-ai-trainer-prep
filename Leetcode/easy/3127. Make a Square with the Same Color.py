# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/make-a-square-with-the-same-color/description/

from typing import List

class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        # Time: O(1)
        # Space: O(1)
        for r in range(2):
            for c in range(2):
                black = white = 0
                for dr in range(2):
                    for dc in range(2):
                        if grid[r + dr][c + dc] == "B":
                            black += 1
                        else:
                            white += 1
                if max(black, white) >= 3:
                    return True
        return False


