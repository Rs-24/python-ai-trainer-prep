

class Solution:
    def findMiddleIndex(self, nums: list) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        l = 0
        r = sum(nums)
        for i, num in enumerate(nums):
            r -= num
            if l == r:
                return i
            l += num
        return -1


