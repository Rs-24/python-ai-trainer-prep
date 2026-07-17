

class Solution:
    def minMoves2(self, nums: list) -> int:
        # Time: O(n log n)
        # Space: O(1)
        nums.sort()
        return sum(abs(x - nums[len(nums) // 2]) for x in nums)


