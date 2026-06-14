

class Solution:
    def canAliceWin(self, nums: list) -> bool:
        # Time: O(n)
        # Space: O(1)
        return sum(n for n in nums if n >= 10) != sum(n for n in nums if n < 10)


