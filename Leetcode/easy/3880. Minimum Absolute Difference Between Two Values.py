# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/minimum-absolute-difference-between-two-values/description/

class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        last_one = last_two = None
        best = float("inf")
        for i, num in enumerate(nums):
            if num == 1:
                if last_two is not None:
                    best = min(best, i - last_two)
                last_one = i
            if num == 2:
                if last_one is not None:
                    best = min(best, i - last_one)
                last_two = i
        return best if best != float("inf") else -1


