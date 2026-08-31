

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # Time: O(n)
        # Space: O(1)
        l = c = a = 0
        for r in range(len(s)):
            c += abs(ord(s[r]) - ord(t[r]))
            while c > maxCost:
                c -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            a = max(a, r - l + 1)
        return a


