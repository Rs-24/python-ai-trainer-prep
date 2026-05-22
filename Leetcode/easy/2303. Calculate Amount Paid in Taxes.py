

class Solution:
    def calculateTax(self, brackets: list[list], income: int) -> float:
        # Time: O(n)
        # Space: O(1)
        total = 0
        prev_u = 0
        for u, p in brackets:
            if income <= prev_u:
                break
            total += (min(income, u) - prev_u) * p / 100
            prev_u = u
        return total


