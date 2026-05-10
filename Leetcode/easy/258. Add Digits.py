
class Solution:
    def addDigits(self, num: int) -> int:
        # Time: O(1)
        # Space: O(1)
        return 0 if num == 0 else (num - 1) % 9 + 1


