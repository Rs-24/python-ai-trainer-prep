

from collections import Counter

class Solution:
    def leastInterval(self, tasks: list, n: int) -> int:
        # Time: O(n)
        # Space: O(n)
        c = Counter(tasks)
        t = max(c.values())
        a = sum(f == t for f in c.values())
        return max((t - 1) * (n + 1) + a, len(tasks))


