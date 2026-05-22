

class Solution:
    def countHillValley(self, nums: list) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        count = 0
        prev = nums[0]
        for i in range(1, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            if prev > nums[i] < nums[i + 1]:
                count += 1
            if prev < nums[i] > nums[i + 1]:
                count += 1
            prev = nums[i]
        return count


