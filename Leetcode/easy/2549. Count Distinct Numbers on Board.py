

class Solution:
    def distinctIntegers(self, n: int) -> int:
        # Time: O(1)
        # Space: O(1)
        if n == 1:
            return 1
        return n - 1


