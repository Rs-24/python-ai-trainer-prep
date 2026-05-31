

class Solution:
    def semiOrderedPermutation(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        return nums.index(1) + len(nums) - nums.index(len(nums)) - 1 - (nums.index(1) > nums.index(len(nums)))


