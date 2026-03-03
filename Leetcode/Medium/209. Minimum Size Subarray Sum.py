# Time to write all of below including tests, explanation and time and aux
# and total space: 15 mins

# Problem: https://leetcode.com/problems/minimum-size-subarray-sum/description/

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        best = float("inf")
        for r, num in enumerate(nums):
            total += num
            while total >= target:
                best = min(best, r - l + 1)
                total -= nums[l]
                l += 1
        return best if best != float("inf") else 0

if __name__ == "__main__":
    sol = Solution()
    assert sol.minSubArrayLen(1, [1]) == 1
    assert sol.minSubArrayLen(2, [1]) == 0
    assert sol.minSubArrayLen(1, [1, 2, 3]) == 1
    assert sol.minSubArrayLen(5, [1, 2, 3]) == 2
    assert sol.minSubArrayLen(3, [1, 1, 1, 2]) == 2
    assert sol.minSubArrayLen(9, [1, 1, 1, 2]) == 0

# Explanation: the code iterates through nums using two pointers while
# incrementing total by num, and shifts the left pointer forward while
# total >= target
# Time: O(n), n = len(nums)
# Space: O(1)


