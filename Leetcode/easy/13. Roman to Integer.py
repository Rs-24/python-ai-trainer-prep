

class Solution:
    def romanToInt(self, s: str) -> int:
        # Time: O(n)
        # Space: O(1)
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        prev = None
        for ch in s:
            res += d[ch]
            if prev is not None and d[prev] < d[ch]:
                res -= d[prev] * 2
            prev = ch
        return res


