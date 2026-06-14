

class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        l_1 = l_2 = -1
        b = float("inf")
        for i, n in enumerate(nums):
            if n == 1:
                if l_2 != -1:
                    b = min(b, i - l_2)
                l_1 = i
            elif n == 2:
                if l_1 != -1:
                    b = min(b, i - l_1)
                l_2 = i
        return b if b != float("inf") else -1


