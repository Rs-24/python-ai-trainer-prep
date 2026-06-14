

class Solution:
    def canAliceWin(self, n: int) -> bool:
        # Time: O(1)
        # Space: O(1)
        c, t = 10, 0
        while n >= c:
            n -= c
            c -= 1
            t += 1
        return t % 2 != 0


