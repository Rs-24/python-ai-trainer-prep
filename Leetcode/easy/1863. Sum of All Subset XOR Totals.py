

class Solution:
    def subsetXORSum(self, nums: list) -> int:
        # Time: O(2 ^ n), n = len(nums)
        # Space: O(n) due to recursion stack
        def dfs(i: int, xor_so_far: int) -> int:
            if i == len(nums):
                return xor_so_far
            cur = xor_so_far ^ nums[i]
            inc = dfs(i + 1, cur)
            exc = dfs(i + 1, xor_so_far)
            return inc + exc
        return dfs(0, 0)


