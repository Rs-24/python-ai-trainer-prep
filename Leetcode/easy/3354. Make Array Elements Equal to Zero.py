

class Solution:
    def countValidSelections(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        l, r = 0, sum(nums)
        c = 0
        for num in nums:
            r -= num
            if num == 0:
                if l == r:
                    c += 2
                elif abs(l - r) == 1:
                    c += 1
            l += num
        return c


