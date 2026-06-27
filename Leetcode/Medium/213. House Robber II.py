

class Solution:
    def rob(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(n)
        if len(nums) == 1:
            return nums[0]
        def r(s: list) -> int:
            a, b = 0, 0
            for x in s:
                t = max(b, a + x)
                a, b = b, t
            return b
        return max(r(nums[:-1]), r(nums[1:]))


