

class Solution:
    def minimumOperations(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(n)
        return len(set(num for num in nums if num != 0))


