

class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        increasing = None
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if diff != 0:
                if increasing is None:
                    increasing = diff > 0
                elif diff > 0 != increasing:
                    return False
        return True


