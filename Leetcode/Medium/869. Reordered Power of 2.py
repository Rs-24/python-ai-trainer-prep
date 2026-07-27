

from collections import Counter

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # Time: O(log n)
        # Space: O(log n)
        c = Counter(str(n))
        for i in range(31):
            if Counter(str(1 << i)) == c:
                return True
        return False


        