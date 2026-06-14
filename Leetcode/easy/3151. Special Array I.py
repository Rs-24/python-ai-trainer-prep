

class Solution:
    def isArraySpecial(self, nums: list) -> bool:
        # Time: O(n)
        # Space: O(1)
        for i in range(1, len(nums)):
            if nums[i - 1] % 2 == nums[i] % 2:
                return False
        return True


