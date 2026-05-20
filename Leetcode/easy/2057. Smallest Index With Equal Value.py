

class Solution:
    def smallestEqual(self, nums: list) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        for i, num in enumerate(nums):
            if num % 10 == i:
                return i
        return -1


