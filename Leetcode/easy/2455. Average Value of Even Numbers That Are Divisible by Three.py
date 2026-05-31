

class Solution:
    def averageValue(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        s = sum(num for num in nums if num % 6 == 0)
        l = sum(1 for num in nums if num % 6 == 0)
        return s // l if l > 0 else 0


