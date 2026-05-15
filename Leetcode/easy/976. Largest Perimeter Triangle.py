

class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        # Time: O(n log n), n = len(nums)
        # Space: O(1)
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]
            if a < b + c:
                return a + b + c
        return 0


