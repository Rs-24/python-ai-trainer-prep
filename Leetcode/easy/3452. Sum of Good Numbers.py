

class Solution:
    def sumOfGoodNumbers(self, nums: list, k: int) -> int:
        # Time: O(n)
        # Space: O(1)
        t = 0
        for i, n in enumerate(nums):
            if 0 <= i - k < len(nums):
                if n <= nums[i - k]:
                    continue
            if 0 <= i + k < len(nums):
                if n <= nums[i + k]:
                    continue
            t += n
        return t


