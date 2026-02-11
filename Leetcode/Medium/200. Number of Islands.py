# Time to write all of below including tests, explanation and time and aux
# and total space: 1h 12 mins

# Problem: https://leetcode.com/problems/number-of-islands/description/

from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total = 0 
        done = []
        q = deque()
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if (y, x) not in done and grid[y][x] == "1":
                    q.append((y, x))
                    while q:
                        j, i = q.popleft()
                        if i >= 1 and grid[j][i - 1] == "1" and (j, i - 1) not in done:
                            q.append((j, i - 1))
                        if i < len(grid[0]) - 1 and grid[j][i + 1] == "1" and (j, i + 1) not in done:
                            q.append((j, i + 1))
                        if j >= 1 and grid[j - 1][i] == "1" and (j - 1, i) not in done:
                            q.append((j - 1, i))
                        if j < len(grid) - 1 and grid[j + 1][i] == "1" and (j + 1, i) not in done:
                            q.append((j + 1, i))
                        done.append((j, i))
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
# finds a 1 whose coordinates are not in done, does a breadth-first-search
# using a queue to find every point in the whole island, while adding each
# island point to done and incrementing total
# Time: O(N), N = number of points in the grid
# Aux space, excluding output and input: O(k), k = number of ones in the grid
# Total space, including output, excluding input: O(k)


