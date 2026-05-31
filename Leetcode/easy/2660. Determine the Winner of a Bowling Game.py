

class Solution:
    def isWinner(self, player1: list, player2: list) -> int:
        # Time: O(n)
        # Space: O(1)
        def score(l: list) -> int:
            t = 0
            for i, s in enumerate(l):
                t += 2 * s if (i > 0 and l[i - 1] == 10) or (i > 1 and l[i - 2] == 10) else s
            return t
        s1, s2 = score(player1), score(player2)
        return 1 if s1 > s2 else 2 if s1 < s2 else 0


