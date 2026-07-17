

from collections import Counter

class Solution:
    def numRabbits(self, answers: list) -> int:
        # Time: O(n)
        # Space: O(1)
        c = Counter(answers)
        a = 0
        for x, f in c.items():
            t = (f + x) // (x + 1)
            a += t * (x + 1)
        return a


