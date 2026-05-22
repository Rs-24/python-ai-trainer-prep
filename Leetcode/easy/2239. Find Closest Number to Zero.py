

class Solution:
    def findClosestNumber(self, nums: list) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        best = float("inf")
        for num in nums:
            if abs(num) < abs(best):
                best = num
            elif abs(num) == abs(best) and num > best:
                best = num
        return best


