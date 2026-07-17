

class Solution:
    def countSubstrings(self, s: str) -> int:
        # Time: O(n^2)
        # Space: O(1)
        n = len(s)
        a = 0
        def e(l: int, r: int) -> int:
            nonlocal a
            while l >= 0 and r < n and s[l] == s[r]:
                a += 1
                l -= 1
                r += 1
        for i in range(n):
            e(i, i)
            e(i, i + 1)
        return a


