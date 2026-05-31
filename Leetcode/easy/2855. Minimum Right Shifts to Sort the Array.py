

class Solution:
    def minimumRightShifts(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        idx = -1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if idx != -1:
                    return -1
                idx = i
        if idx == -1:
            return 0
        if nums[0] < nums[-1]:
            return -1
        return len(nums) - idx


