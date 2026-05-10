

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        l = 0
        for r, num in enumerate(nums):
            if nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums
    

