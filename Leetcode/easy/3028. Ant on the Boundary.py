

class Solution:
    def returnToBoundaryCount(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        c = 0
        p = 0
        for n in nums:
            p += n
            c += p == 0
        return c


