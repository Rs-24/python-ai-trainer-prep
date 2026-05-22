

class Solution:
    def fillCups(self, amount: list) -> int:
        # Time: O(n)
        # Space: O(1)
        return max(max(amount), (sum(amount) + 1) // 2)


