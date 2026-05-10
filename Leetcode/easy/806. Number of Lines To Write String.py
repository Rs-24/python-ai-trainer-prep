

class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        # Time: O(n), n = len(widths)
        # Space: O(1)
        l = 1
        w = 0
        for ch in s:
            cur = widths[ord(ch) - ord("a")]
            if w + cur > 100:
                l += 1
                w = cur
            else:
                w += cur
        return [l, w]


