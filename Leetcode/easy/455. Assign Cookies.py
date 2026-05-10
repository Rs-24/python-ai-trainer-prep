

class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        # Time: O(m log m + n log n), m = len(g), n = len(s)
        # Space: O(1)
        g.sort()
        s.sort()
        i = j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
            j += 1
        return i


