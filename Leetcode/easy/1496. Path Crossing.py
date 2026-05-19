

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # Time: O(n), n = len(path)
        # Space: O(n)
        s = set()
        x = y = 0
        for ch in path:
            s.add((x, y))
            x += 1 if ch == "E" else -1 if ch == "W" else 0
            y += 1 if ch == "N" else -1 if ch == "S" else 0
            if (x, y) in s:
                return True
        return False


