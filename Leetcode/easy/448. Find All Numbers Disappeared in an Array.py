

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
        out = []
        for i, num in enumerate(nums):
            if num > 0:
                out.append(i + 1)
        return out


