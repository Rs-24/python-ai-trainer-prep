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

# Learning lessons (done after completing all of above in 1h 12 mins):
#   - I now realise my solution can be improved, my rewrite is below:
#
# def numIslands(self, grid: List[List[str]]) -> int:
#     # Time: O(N), N = number of points in grid
#     # Aux space, excluding output and input: O(k), k = number of "1"'s in
#     # grid, worst case O(N)
#     # Total space, including output, excluding input: O(k), worst case O(N)
#     total = 0 
#     visited = set()
#     q = deque()
#     for y in range(len(grid)):
#         for x in range(len(grid[0])):
#             if (y, x) not in visited and grid[y][x] == "1":
#                 q.append((y, x))
#                 visited.add((y, x))
#                 while q:
#                     j, i = q.popleft()
#                     for dj, di in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
#                         new_j = j + dj
#                         new_i = i + di
#                         if 0 <= new_j < len(grid) and 0 <= new_i < len(grid[0]) and grid[new_j][new_i] == "1" and (new_j, new_i) not in visited:
#                             q.append((new_j, new_i))
#                             visited.add((new_j, new_i))
#                 total += 1
#     return total
#
#   - Additionally, there is also a depth-first-search version of the above,
#     my attempt is below:
#
# def numIslands(self, grid: List[List[str]]) -> int:
#     # Time: O(N), N = number of points in grid
#     # Aux space, excluding output and input: O(k), k = number of 1's in grid,
#     # worst case O(N) if grid consists of only 1's
#     # Total space, including output, excluding input: O(k), worst case O(N)
#     total = 0
#     visited = set()
#     stack = []
#     for y in range(len(grid)):
#         for x in range(len(grid[0])):
#             if (y, x) not in visited and grid[y][x] == "1":
#                 stack.append((y, x))
#                 visited.add((y, x))
#                 while stack:
#                     j, i = stack.pop()
#                     for dj, di in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#                         new_j = j + dj
#                         new_i = i + di
#                         if 0 <= new_j < len(grid) and 0 <= new_i < len(grid[0]) and (new_j, new_i) not in visited and grid[new_j][new_i] == "1":
#                             stack.append((new_j, new_i))
#                             visited.add((new_j, new_i))
#                 total += 1
#     return total
#
#   - Additionally, there is also an iterative breadth-first-search method
#     without using a set by changing 1's to 0's. My attempt is below:  
#
# def numIslands(self, grid: List[List[str]]) -> int:
#     # Time: O(N), N = number of points in grid
#     # Aux space, excluding output and input: O(Q), Q = max size reached by queue,
#     # worst case O(N) if grid only consists of 1's
#     # Total space, including output, excluding input: O(Q), worst case O(N)
#     total = 0
#     q = deque()
#     for y in range(len(grid)):
#         for x in range(len(grid[0])):
#             if grid[y][x] == "1":
#                 q.append((y, x))
#                 grid[y][x] = "0"          
#                 while q:
#                     j, i = q.popleft()
#                     for dj, di in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#                         new_j = j + dj
#                         new_i = i + di
#                         if 0 <= new_j < len(grid) and 0 <= new_i < len(grid[0]) and grid[new_j][new_i] == "1":
#                             q.append((new_j, new_i))
#                             grid[new_j][new_i] = "0"
#                 total += 1    
#     return total
#
#   - Additionally, there is also an iterative depth-first-search method
#     without using a set by changing 1's to 0's. My attempt is below:
#
# def numIslands(self, grid: List[List[str]]) -> int:
#     # Time: O(N), N = number of points in grid
#     # Aux space, excluding output and input: O(k), k = max size reached by
#     # stack, worst case O(N) if grid only consists of 1's 
#     # Total space, including output, excluding and input: O(k), worst case O(N) 
#     stack = []
#     total = 0
#     for y in range(len(grid)):
#         for x in range(len(grid[0])):
#             if grid[y][x] == "1":
#                 stack.append((y, x))
#                 grid[y][x] = "0"
#                 while stack:
#                     j, i = stack.pop()       
#                     for dj, di in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#                         new_j = j + dj
#                         new_i = i + di
#                         if 0 <= new_j < len(grid) and 0 <= new_i < len(grid[0]) and grid[new_j][new_i] == "1":
#                             stack.append((new_j, new_i))
#                             grid[new_j][new_i] = "0"
#                 total += 1
#     return total
#
#   - Additionally, there is also a recursive depth-first-search method
#     without using a set by changing 1's to 0's. My attempt is below:
#
# def numIslands(self, grid: List[List[str]]) -> int:
#     # Time: O(N), N = number of points in the grid
#     # Aux space, excluding output and input: worst case O(N) due to recursion
#     # stack if grid only consists of 1's
#     # Total space, including output, excluding input: worst case O(N)
#     total = 0
#     def dfs(j: int, i: int) -> None:
#         if 0 <= j < len(grid) and 0 <= i < len(grid[0]) and grid[j][i] == "1":
#             grid[j][i] = "0"
#             for dj, di in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#                 new_j = j + dj
#                 new_i = i + di
#                 dfs(new_j, new_i)
#     for y in range(len(grid)):
#         for x in range(len(grid[0])):
#             if grid[y][x] == "1":
#                 dfs(y, x)
#                 total += 1
#     return total



























