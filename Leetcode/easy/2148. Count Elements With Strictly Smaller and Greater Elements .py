

class Solution:
    def countElements(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        l, h = min(nums), max(nums)
        return sum(1 for num in nums if num > l and num < h)


