

class Solution:
    def countPairs(self, nums: list, target: int) -> int:
        # Time: O(n log n)
        # Space: O(1)
        nums.sort()
        l, r = 0, len(nums) - 1
        c = 0
        while l < r:
            if nums[l] + nums[r] < target:
                c += (r - l)
                l += 1
            else:
                r -= 1
        return c


