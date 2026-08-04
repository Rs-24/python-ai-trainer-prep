

class Solution:
    def partitionDisjoint(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        l, m, j = nums[0], nums[0], 0 
        for i in range(1, len(nums)):
            m = max(m, nums[i])
            if nums[i] < l:
                j = i
                l = m
        return j + 1


        