

from functools import lru_cache 

class Solution:
    def predictTheWinner(self, nums: list) -> bool:
        # Time: O(n^2)
        # Space: O(n^2)
        @lru_cache(None)
        def dfs(i: int, j: int) -> int:
            if i == j:
                return nums[i]
            return max(nums[i] - dfs(i + 1, j), nums[j] - dfs(i, j - 1))
        return dfs(0, len(nums) - 1) >= 0


