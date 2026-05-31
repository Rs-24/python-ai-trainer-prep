

class Solution:
    def findNonMinOrMax(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        l, h = min(nums), max(nums)
        for num in nums:
            if num != l and num != h:
                return num
        return -1


