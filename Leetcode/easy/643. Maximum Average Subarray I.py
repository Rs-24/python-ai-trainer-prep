

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        total = 0
        for i in range(k):
            total += nums[i]
        best = total
        for i in range(k, len(nums)):
            total -= nums[i - k]
            total += nums[i]
            best = max(best, total)
        return best / k


