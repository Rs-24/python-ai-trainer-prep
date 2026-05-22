

from collections import Counter

class Solution:
    def digitCount(self, num: str) -> bool:
        # Time: O(n)
        # Space: O(n)
        c = Counter(num)
        return all(c[str(i)] == int(d) for i, d in enumerate(num))


