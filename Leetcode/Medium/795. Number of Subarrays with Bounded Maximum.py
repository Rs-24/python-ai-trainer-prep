

class Solution:
    def numSubarrayBoundedMax(self, nums: list, left: int, right: int) -> int:
        # Time: O(n)
        # Space: O(1)
        i = ni = -1
        a = 0
        for j, x in enumerate(nums):
            if x > right:
                ni = j
            if left <= x <= right:
                i = j
            a += max(0, i - ni)
        return a


