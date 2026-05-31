

class Solution:
    def maximumTripletValue(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        max_l = 0
        max_diff = 0
        b = 0
        for num in nums:
            b = max(b, max_diff * num)
            max_diff = max(max_diff, max_l - num)
            max_l = max(max_l, num)
        return b


