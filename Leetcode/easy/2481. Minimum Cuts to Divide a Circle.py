

class Solution:
    def numberOfCuts(self, n: int) -> int:
        # Time: O(1)
        # Space: O(1)
        if n == 1:
            return 0
        return n // 2 if n % 2 == 0 else n


