

class Solution:
    def maxProduct(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        if not nums:
            return 0
        ma = mi = a = nums[0]
        for i in range(1, len(nums)):
            ta = max(nums[i], nums[i] * ma, nums[i] * mi)
            ti = min(nums[i], nums[i] * ma, nums[i] * mi)
            ma, mi = ta, ti
            a = max(a, ma)
        return a


