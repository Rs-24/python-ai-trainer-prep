

class Solution:
    def distinctAverages(self, nums: list) -> int:
        # Time: O(n log n)
        # Space: O(n)
        nums.sort()
        s = set()
        l, r = 0, len(nums) - 1
        while l < r:
            s.add((nums[l] + nums[r]) / 2)
            l += 1
            r -= 1
        return len(s)


