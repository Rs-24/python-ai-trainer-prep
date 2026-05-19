

class Solution:
    def arraySign(self, nums: list) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        sign = 1
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                sign *= -1
        return sign


