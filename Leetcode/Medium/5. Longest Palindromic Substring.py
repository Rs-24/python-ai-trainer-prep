

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Time: O(n^2)
        # Space: O(n)
        def expand(a: int, b: int) -> tuple[int, int]:
            while a >= 0 and b < len(s) and s[a] == s[b]:
                a -= 1
                b += 1
            return a + 1, b - 1
        l = r = 0
        for i in range(len(s)):
            a, b = expand(i, i)
            if b - a > r - l:
                l, r = a, b
            a, b = expand(i, i + 1)
            if b - a > r - l:
                l, r = a, b
        return s[l:r + 1]


