

class Solution:
    def findUnsortedSubarray(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        n = len(nums)
        t = float("-inf")
        r = -1
        for i in range(n):
            t = max(t, nums[i])
            if nums[i] < t:
                r = i
        t = float("inf")
        l = -1
        for i in range(n - 1, -1, -1):
            t = min(t, nums[i])
            if nums[i] > t:
                l = i
        if r == -1:
            return 0
        return r - l + 1


