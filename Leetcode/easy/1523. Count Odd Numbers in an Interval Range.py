

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Time: O(1)
        # Space: O(1)
        return (high + 1) // 2 - (low // 2)


