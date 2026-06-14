

class Solution:
    def missingInteger(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(n)
        t = nums[0]
        i = 0
        while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
            t += nums[i + 1]
            i += 1
        s = set(nums)
        while t in s:
            t += 1
        return t


