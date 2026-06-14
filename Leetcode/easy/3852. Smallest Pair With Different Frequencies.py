

from collections import Counter

class Solution:
    def minDistinctFreqPair(self, nums: list) -> list:
        # Time: O(n^2 + n log n)
        # Space: O(n)
        c = Counter(nums)
        k = sorted(c.keys())
        for i in range(len(k)):
            for j in range(i + 1, len(k)):
                if c[k[i]] != c[k[j]]:
                    return [k[i], k[j]]
        return [-1, -1]


