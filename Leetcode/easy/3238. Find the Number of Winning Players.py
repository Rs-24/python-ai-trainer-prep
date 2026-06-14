

class Solution:
    def winningPlayerCount(self, n: int, pick: list[list]) -> int:
        # Time: O(n)
        # Space: O(n)
        c = [[0] * 11 for _ in range(n)]
        for x, y in pick:
            c[x][y] += 1
        return sum(max(c[x]) > x for x in range(n))


