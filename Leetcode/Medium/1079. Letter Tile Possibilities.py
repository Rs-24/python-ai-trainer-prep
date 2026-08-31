

from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # Time: O(n)
        # Space: O(n)
        c = Counter(tiles)
        def dfs() -> int:
            t = 0
            for ch in c:
                if c[ch] == 0:
                    continue
                t += 1
                c[ch] -= 1
                t += dfs()
                c[ch] += 1
            return t
        return dfs()


