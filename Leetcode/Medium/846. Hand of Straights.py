

from collections import Counter

class Solution:
    def isNStraightHand(self, hand: list, groupSize: int) -> bool:
        # Time: O(n log n)
        # Space: O(n)
        if len(hand) % groupSize != 0:
            return False
        c = Counter(hand)
        for x in sorted(c):
            if c[x] > 0:
                for y in range(x, x + groupSize):
                    if c[y] < c[x]:
                        return False
                    c[y] -= c[x]
        return True


        