

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Time: O((h - n + 1) * n), h = len(haystack), n = len(needle)
        # Space: O(n)
        h, n = len(haystack), len(needle)
        if h < n:
            return -1
        for i in range(h - n + 1):
            if haystack[i:i + n] == needle:
                return i
        return -1


