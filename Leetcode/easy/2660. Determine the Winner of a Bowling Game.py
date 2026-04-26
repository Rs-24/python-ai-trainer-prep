# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/description/

from typing import List

class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        # Time: O(n), n = len(player1) = len(player2)
        # Space: O(1)
        def score(p: List[int]) -> int:
            total = 0
            for i, s in enumerate(p):
                if (i > 0 and p[i - 1] == 10) or (i > 1 and p[i - 2] == 10):
                    total += 2 * s
                else:
                    total += s
            return total
        p1 = score(player1)
        p2 = score(player2)
        if p1 > p2:
            return 1
        elif p1 < p2:
            return 2
        return 0


