

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        l = 0
        for r in range(1, len(nums)):
            if nums[l] != nums[r]:
                l += 1
                nums[l], nums[r] = nums[r], nums[l]
        return l + 1


