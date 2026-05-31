

class Solution:
    def findMaxK(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(n)
        s = set(nums)
        best = -1
        for num in nums:
            if num > 0 and -num in s:
                best = max(best, num)
        return best


