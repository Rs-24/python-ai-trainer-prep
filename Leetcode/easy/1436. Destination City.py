

class Solution:
    def destCity(self, paths: list[list]) -> str:
        # Time: O(n), n = len(paths)
        # Space: O(n)
        s = set()
        for a, _ in paths:
            s.add(a)
        for _, b in paths:
            if b not in s:
                return b


