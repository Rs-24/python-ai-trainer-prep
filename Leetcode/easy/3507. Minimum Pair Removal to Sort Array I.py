

class Solution:
    def minimumPairRemoval(self, nums: list) -> int:
        # Time: O(n^2)
        # Space: O(1)
        def is_sorted(a: list) -> bool:
            for i in range(1, len(a)):
                if a[i - 1] > a[i]:
                    return False
            return True
        c = 0
        while not is_sorted(nums):
            m = nums[0] + nums[1]
            idx = 0
            for i in range(1, len(nums) - 1):
                t = nums[i] + nums[i + 1]
                if t < m:
                    m = t
                    idx = i
            nums[idx] = m
            nums.pop(idx + 1)
            c += 1
        return c


