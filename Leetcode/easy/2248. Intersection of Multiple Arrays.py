

class Solution:
    def intersection(self, nums: list[list]) -> list:#
        # Time: O(n log n)
        # Space: O(n)
        s = set(nums[0])
        for i in range(1, len(nums)):
            s &= set(nums[i])
        return sorted(list(s))


