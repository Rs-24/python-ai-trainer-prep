

class Solution:
    def longestOnes(self, nums: list, k: int) -> int:
        # Time: O(n)
        # Space: O(1)
        l = z = a = 0
        for r in range(len(nums)):
            z += nums[r] == 0
            while z > k:
                z -= nums[l] == 0
                l += 1
            a = max(a, r - l + 1)
        return a


        