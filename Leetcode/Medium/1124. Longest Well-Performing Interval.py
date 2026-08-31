

class Solution:
    def longestWPI(self, hours: list) -> int:
        # Time: O(n)
        # Space: O(n)
        t, a, d = 0, 0, {}
        for i, h in enumerate(hours):
            t += 1 if h > 8 else -1
            if t > 0:
                a = i + 1
            elif t - 1 in d:
                a = max(a, i - d[t - 1])
            if t not in d:
                d[t] = i
        return a


