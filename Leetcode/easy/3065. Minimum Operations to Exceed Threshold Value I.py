

class Solution:
    def minOperations(self, nums: list, k: int) -> int:
        # Time: O(n)
        # Space: O(1)
        return sum(1 for n in nums if n < k)


