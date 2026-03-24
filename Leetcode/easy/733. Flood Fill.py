# Time to write all of below including tests, explanation and time and aux
# and total space: 12 mins

# Problem: https://leetcode.com/problems/flood-fill/description/

from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Time: O(n), n = number of cells in image
        # Space: O(n)
        starting_color = image[sr][sc]
        if starting_color == color:
            return image
        stack = [(sr, sc)]
        while stack:
            r, c = stack.pop()
            if not (0 <= r < len(image) and 0 <= c < len(image[0])):
                continue
            if image[r][c] == starting_color:
                image[r][c] = color
                stack.append((r + 1, c))
                stack.append((r - 1, c))
                stack.append((r, c + 1))
                stack.append((r, c - 1))
        return image

# Recursive method:
from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Time: O(n), n = number of cells in image
        # Space: O(n) due to recursion stack
        starting_color = image[sr][sc]
        if starting_color == color:
            return image
        def dfs(a: int, b: int) -> None:
            if not (0 <= a < len(image) and 0 <= b < len(image[0])):
                return None
            if image[a][b] == starting_color:
                image[a][b] = color
                dfs(a + 1, b)
                dfs(a - 1, b)
                dfs(a, b + 1)
                dfs(a, b - 1)
        dfs(sr, sc)
        return image


