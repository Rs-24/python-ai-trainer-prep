

class Solution:
    def minIncrementForUnique(self, nums: list) -> int:
        # Time: O(n log n)
        # Space: O(1)
        nums.sort()
        a, t = 0, nums[0]
        for x in nums:
            if x < t:
                a += t - x
            else:
                t = x
            t += 1
        return a


