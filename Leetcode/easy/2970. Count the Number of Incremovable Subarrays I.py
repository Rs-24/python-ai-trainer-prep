

class Solution:
    def incremovableSubarrayCount(self, nums: list) -> int:
        # Time: O(n^3)
        # Space: O(n)
        c = 0
        for l in range(len(nums)):
            for r in range(l, len(nums)):
                a = nums[:l] + nums[r + 1:]
                c += 1 if all(a[i] < a[i + 1] for i in range(len(a) - 1)) else 0
        return c


