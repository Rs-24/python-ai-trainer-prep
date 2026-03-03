# Time to write all of below including tests, explanation and time and aux
# and total space: 38 mins

# Problem: https://leetcode.com/problems/number-of-islands/description/

from typing import List 
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        total = 0
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if (x, y) not in seen and grid[y][x] == "1":
                    q = deque([(x, y)])
                    while q:
                        a, b = q.popleft()
                        if 0 <= a < len(grid[0]) and 0 <= b < len(grid):
                            if (a, b) not in seen and grid[b][a] == "1":
                                seen.add((a, b))
                                for da, db in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                                    q.append((a + da, b + db))
                    total += 1
        return total

if __name__ == "__main__":
    sol = Solution()

    grid = [["1"]]
    assert sol.numIslands(grid) == 1

    grid = [["0"]]
    assert sol.numIslands(grid) == 0

    grid = [["1"],
            ["1"]]
    assert sol.numIslands(grid) == 1

    grid = [["1", "0"],
            ["0", "1"]]
    assert sol.numIslands(grid) == 2

    grid = [["1", "0"],
            ["0", "1"],
            ["1", "0"]]
    assert sol.numIslands(grid) == 3

    grid = [["1", "1", "1"],
            ["1", "0", "1"],
            ["1", "1", "1"]]
    assert sol.numIslands(grid) == 1

    grid = [["0", "0", "0"],
            ["0", "0", "0"],
            ["0", "0", "0"]]
    assert sol.numIslands(grid) == 0

    grid = [["1", "1", "0", "1"],
            ["1", "0", "1", "0"],
            ["0", "1", "0", "1"],
            ["1", "0", "1", "1"]]
    assert sol.numIslands(grid) == 6

# Explanation: the code iterates through every point in the grid, and if it
# finds a 1 whose coordinates are not in seen, does a breadth-first-search
# using a queue to find every point in the whole island, while adding each
# island point to seen and incrementing total
# Time: O(N), N = number of nodes in grid
# Space: worst case O(N)

# Depth-first-search method:
from typing import List 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time: O(N), N = number of nodes in grid
        # Space: worst case O(N)
        seen = set()
        total = 0
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if (x, y) not in seen and grid[y][x] == "1":
                    stack = [(x, y)]
                    while stack:
                        a, b = stack.pop()
                        if 0 <= a < len(grid[0]) and 0 <= b < len(grid):
                                if grid[b][a] == "1" and (a, b) not in seen:
                                    seen.add((a, b))
                                    for da, db in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                                        stack.append((a + da, b + db))
                    total += 1
        return total

# Iterative breadth-first-search method without using a set by changing
# 1's to 0's:
from typing import List 
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time: O(m * n), m = number of rows, n = number of columns
        # Space: O(L), L = number of points in largest island, worst case O(m * n)
        total = 0
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if grid[y][x] == "1":
                    q = deque([(x, y)])
                    while q:
                        a, b = q.popleft()
                        if 0 <= a < len(grid[0]) and 0 <= b < len(grid):
                            if grid[b][a] == "1":
                                grid[b][a] = "0"
                                for da, db in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                                    q.append((a + da, b + db))
                    total += 1
        return total

# Iterative depth-first-search method without using a set by changing
# 1's to 0's:
from typing import List 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time: O(m * n), m = number of rows, n = number of columns
        # Space: O(L), L = number of points in largest island, worst case O(m * n)
        total = 0
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if grid[y][x] == "1":
                    stack = [(x, y)]
                    while stack:
                        a, b = stack.pop()
                        if 0 <= a < len(grid[0]) and 0 <= b < len(grid):
                            if grid[b][a] == "1":
                                grid[b][a] = "0"
                                for da, db in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                                    stack.append((a + da, b + db))
                    total += 1
        return total

# Recursive depth-first-search method without using a set by changing
# 1's to 0's:
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time: O(m * n), m = number of rows, n = number of columns
        # Space: O(L) due to recursion stack, L = number of points in largest
        # island, worst case O(m * n)
        total = 0
        def dfs(a: int, b: int) -> None:
            if 0 <= a < len(grid[0]) and 0 <= b < len(grid):
                if grid[b][a] == "1":
                    grid[b][a] = "0"
                    for da, db in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        dfs(a + da, b + db)
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if grid[y][x] == "1":
                    dfs(x, y)
                    total += 1
        return total


