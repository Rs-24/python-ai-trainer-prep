

from collections import Counter

class Solution:
    def kthDistinct(self, arr: list, k: int) -> str:
        # Time: O(n), n = len(arr)
        # Space: O(n)
        c = Counter(arr)
        for a in arr:
            if c[a] == 1:
                k -= 1
                if k == 0:
                    return a
        return ""


