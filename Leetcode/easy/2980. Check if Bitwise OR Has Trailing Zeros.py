

class Solution:
    def hasTrailingZeros(self, nums: list) -> bool:
        # Time: O(n)
        # Space: O(1)
        return sum(n % 2 == 0 for n in nums) >= 2


