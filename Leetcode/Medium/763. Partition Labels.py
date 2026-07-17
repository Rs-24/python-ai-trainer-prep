

class Solution:
    def partitionLabels(self, s: str) -> list:
        # Time: O(n)
        # Space: O(n)
        d = {ch: i for i, ch in enumerate(s)}
        o = []
        a = b = 0
        for i, ch in enumerate(s):
            b = max(b, d[ch])
            if i == b:
                o.append(b - a + 1)
                a = i + 1
        return o


