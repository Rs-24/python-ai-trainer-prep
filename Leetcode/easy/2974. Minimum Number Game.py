

class Solution:
    def numberGame(self, nums: list) -> list:
        # Time: O(n log n)
        # Space: O(1)
        nums.sort()
        for i in range(0, len(nums), 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums


