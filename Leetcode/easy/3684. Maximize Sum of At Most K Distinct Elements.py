

class Solution:
    def maxKDistinct(self, nums: list, k: int) -> list:
        # Time: O(n log n)
        # Space: O(n)
        return sorted(list(set(nums)), reverse=True)[:k]


