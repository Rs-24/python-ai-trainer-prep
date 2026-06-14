

class Solution:
    def jump(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        c = f = e = 0
        for i in range(len(nums) - 1):
            f = max(f, i + nums[i])
            c += i == e
            e = f if i == e else e
        return c


