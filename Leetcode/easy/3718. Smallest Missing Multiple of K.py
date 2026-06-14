

class Solution:
    def missingMultiple(self, nums: list, k: int) -> int:
        # Time: O(n)
        # Space: O(n)
        s = set(nums)
        m = 1
        while m * k in s:
            m += 1
        return m * k


