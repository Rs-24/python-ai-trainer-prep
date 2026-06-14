

class Solution:
    def minimumOperations(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        return sum(min(n % 3, 3 - n % 3) for n in nums)


