

class Solution:
    def transformArray(self, nums: list) -> list:
        # Time: O(n)
        # Space: O(n)
        return [0] * sum(n % 2 == 0 for n in nums) + [1] * sum(n % 2 != 0 for n in nums)


