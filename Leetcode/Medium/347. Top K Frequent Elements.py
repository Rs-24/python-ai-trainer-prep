

from collections import Counter

class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        # Time: O(n)
        # Space: O(n)
        c = Counter(nums)
        b = [[] for _ in range(len(nums) + 1)]
        for x, f in c.items():
            b[f].append(x)
        out = []
        for i in range(len(b) - 1, -1, -1):
            for x in b[i]:
                out.append(x)
                if len(out) == k:
                    return out


