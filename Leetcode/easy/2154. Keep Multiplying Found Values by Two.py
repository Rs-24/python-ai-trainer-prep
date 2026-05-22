

class Solution:
    def findFinalValue(self, nums: list, original: int) -> int:
        # Time: O(n)
        # Space: O(n)
        s = set(nums)
        while original in s:
            original *= 2
        return original


