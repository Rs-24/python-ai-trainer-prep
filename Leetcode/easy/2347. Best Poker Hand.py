

from collections import Counter

class Solution:
    def bestHand(self, ranks: list, suits: list) -> str:
        # Time: O(1)
        # Space: O(1)
        if len(set(suits)) == 1:
            return "Flush"
        c = Counter(ranks)
        best = max(c.values())
        return "Three of a Kind" if best >= 3 else "Pair" if best >= 2 else "High Card"


