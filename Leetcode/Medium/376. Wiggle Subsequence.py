

class Solution:
    def wiggleMaxLength(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        if not nums:
            return 0
        u = d = 1
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                d = u + 1
            elif nums[i - 1] < nums[i]:
                u = d + 1
        return max(u, d)


