

from collections import Counter

class Solution:
    def largestValsFromLabels(self, values: list, labels: list, numWanted: int, useLimit: int) -> int:
        # Time: O(n log n)
        # Space: O(n)
        s = sorted(zip(values, labels) , reverse=True)
        c, a, t = Counter(), 0, 0
        for v, l in s:
            if c[l] >= useLimit:
                continue
            a += v
            c[l] += 1
            t += 1
            if t == numWanted:
                break
        return a


