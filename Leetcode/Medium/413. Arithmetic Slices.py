

class Solution:
    def numberOfArithmeticSlices(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        n = len(nums)
        if n < 3:
            return 0
        c = t = 0
        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                t += 1
                c += t
            else:
                t = 0
        return c


