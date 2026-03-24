# Time to write all of below including tests, explanation and time and aux
# and total space: 16 mins

# Problem: https://leetcode.com/problems/island-perimeter/description/

from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Time: O(n), n = number of cells in grid
        # Space: O(n)
        seen = set()
        total = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    stack = [(r, c)]
                    seen.add((r, c))
                    while stack:
                        row, column = stack.pop()
                        temp = 4
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            if 0 <= row + dr < len(grid) and 0 <= column + dc < len(grid[0]) and grid[row + dr][column + dc] == 1:
                                temp -= 1
                                if (row + dr, column + dc) not in seen:
                                    stack.append((row + dr, column + dc))
                                    seen.add((row + dr, column + dc))
                        total += temp
                    return total

# Non graph traversal method:
from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Time: O(n), n = number of cells in grid
        # Space: O(1)
        total = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    temp = 4
                    if r > 0 and grid[r - 1][c] == 1:
                        temp -= 2
                    if c > 0 and grid[r][c - 1] == 1:
                        temp -= 2
                    total += temp
        return total

# Recursive depth-first-search version:
from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Time: O(n), n = number of nodes in grid
        # Space: O(n) due to recursion stack
        def dfs(x: int, y: int) -> int:
            if not (0 <= x < len(grid[0]) and 0 <= y < len(grid)):
                return 1
            if grid[y][x] == 0:
                return 1
            if grid[y][x] == -1:
                return 0
            grid[y][x] = -1
            return dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y - 1) + dfs(x, y + 1)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return dfs(c, r)


