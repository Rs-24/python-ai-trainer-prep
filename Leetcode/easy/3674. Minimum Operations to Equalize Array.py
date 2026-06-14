

class Solution:
    def minOperations(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        return 0 if all(n == nums[0] for n in nums) else 1


