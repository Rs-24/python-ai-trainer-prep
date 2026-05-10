

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        l = 0
        for r, num in enumerate(nums):
            if num != val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return l


