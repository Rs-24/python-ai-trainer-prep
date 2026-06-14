

class Solution:
    def minOperations(self, nums: list, k: int) -> int:
        # Time: O(n)
        # Space: O(1)
        return sum(nums) % k


