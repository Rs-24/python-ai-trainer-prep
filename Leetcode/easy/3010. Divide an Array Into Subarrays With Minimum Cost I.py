

class Solution:
    def minimumCost(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        a = b = float("inf")
        for i in range(1, len(nums)):
            if nums[i] <= a:
                b = a
                a = nums[i]
            elif nums[i] <= b:
                b = nums[i]
        return nums[0] + a + b


