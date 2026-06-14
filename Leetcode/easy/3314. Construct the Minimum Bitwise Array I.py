

class Solution:
    def minBitwiseArray(self, nums: list) -> list:
        # Time: O(n)
        # Space: O(n)
        return [n - (n & -n) for n in nums]


