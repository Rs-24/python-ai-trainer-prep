

from collections import Counter

class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        return s


