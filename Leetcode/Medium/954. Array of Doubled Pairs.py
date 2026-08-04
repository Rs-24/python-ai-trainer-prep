

from collections import Counter

class Solution:
    def canReorderDoubled(self, arr: list) -> bool:
        # Time: O(n log n)
        # Space: O(n)
        c = Counter(arr)
        for x in sorted(c, key=abs):
            if c[x] > c[2 * x]:
                return False
            c[2 * x] -= c[x]
        return True


        