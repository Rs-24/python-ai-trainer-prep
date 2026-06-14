

class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        return sum(nums[i] == 0 for i in range(len(nums) - nums.count(0)))


