

class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        # Time: O(n log n + n^2)
        # Space: O(1)
        nums.sort()
        b = float("inf")
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if abs(nums[i] + nums[l] + nums[r] - target) < abs(b - target):
                    b = nums[i] + nums[l] + nums[r]
                if nums[i] + nums[l] + nums[r] < target:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > target:
                    r -= 1
                else:
                    return target
        return b


