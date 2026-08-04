

class Solution:
    def maxWidthRamp(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(n)
        s = []
        for i, x in enumerate(nums):
            if not s or nums[s[-1]] > x:
                s.append(i)
        a = 0
        for i in range(len(nums) - 1, -1, -1):
            while s and nums[s[-1]] <= nums[i]:
                a = max(a, i - s.pop())
        return a


        