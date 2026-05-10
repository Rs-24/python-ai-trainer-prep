

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        need = {}
        for i, num in enumerate(nums):
            if target - num in need:
                return [need[target - num], i]
            need[num] = i


