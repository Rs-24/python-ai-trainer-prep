# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/path-crossing/description/

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # Time: O(n), n = len(path)
        # Space: O(n)
        visited = set()
        visited.add((0, 0))
        x = 0
        y = 0
        for ch in path:
            x += 1 if ch == "E" else -1 if ch == "W" else 0
            y += 1 if ch == "N" else -1 if ch == "S" else 0
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False


