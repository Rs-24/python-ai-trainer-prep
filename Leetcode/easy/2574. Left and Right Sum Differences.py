

class Solution:
    def leftRightDifference(self, nums: list) -> list:
        # Time: O(n)
        # Space: O(n)
        l, r = 0, sum(nums)
        out = []
        for num in nums:
            r -= num
            out.append(abs(l - r))
            l += num
        return out


