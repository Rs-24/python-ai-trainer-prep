

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # Time: O(n)
        # Space: O(1)
        c = [0] * 26
        l = b = 0
        for r, ch in enumerate(s):
            c[ord(ch) - ord("a")] += 1
            while c[ord(s[l]) - ord("a")] > 2:
                c[ord(s[l]) - ord("a")] -= 1
                l += 1
            b = max(b, r - l + 1)
        return b


