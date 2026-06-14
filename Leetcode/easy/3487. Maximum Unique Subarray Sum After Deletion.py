

class Solution:
    def maxSum(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(n)
        if max(nums) <= 0:
            return max(nums)
        s = set()
        t = 0
        for n in nums:
            if n > 0 and n not in s:
                t += n
                s.add(n)
        return t


