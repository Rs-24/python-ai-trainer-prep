

class Solution:
    def maxOperations(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        need = nums[0] + nums[1]
        c = 1
        for i in range(2, len(nums) - 1, 2):
            if nums[i] + nums[i + 1] != need:
                break
            c += 1
        return c


