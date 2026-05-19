

class Solution:
    def totalMoney(self, n: int) -> int:
        # Time: O(n)
        # Space: O(1)
        total = 0
        day = 1
        while day <= n:
            week = (day - 1) // 7
            total += week + 1 + (day - 1) % 7
            day += 1
        return total


