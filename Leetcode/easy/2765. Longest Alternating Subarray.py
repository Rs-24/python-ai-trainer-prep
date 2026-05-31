

class Solution:
    def alternatingSubarray(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        best = -1
        cur = 1
        diff = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == diff:
                cur += 1
                diff *= - 1
                best = max(best, cur)
            else:
                if nums[i + 1] - nums[i] == 1:
                    cur = 2
                    diff = -1
                    best = max(best, cur)
                else:
                    cur = 1
                    diff = 1
        return best


