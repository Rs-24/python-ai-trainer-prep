

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time: O(n)
        # Space: O(n)
        w = set()
        l = 0
        b = 0
        for r, ch in enumerate(s):
            while ch in w:
                w.remove(s[l])
                l += 1
            w.add(ch)
            b = max(b, r - l + 1)
        return b


