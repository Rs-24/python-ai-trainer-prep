

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        # Time: O(1)
        # Space: O(1)
        return num == 0 or num % 10 != 0


