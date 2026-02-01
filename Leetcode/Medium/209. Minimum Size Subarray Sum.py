# Time to write all of below including tests, explanation and time and aux
# and total space: 15 mins

# Problem: https://leetcode.com/problems/minimum-size-subarray-sum/description/

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lowest = None
        for i in range(len(nums)):
            total = nums[i]
            arr_len = 1
            if nums[i] == target:
                return 1
            for j in range(len(nums)):
                if j <= i:
                    continue
                total += nums[j]
                arr_len += 1
                if total >= target:
                    if not lowest:
                        lowest = arr_len
                    else:
                        lowest = min(lowest, arr_len)
        return 0 if not lowest else lowest

if __name__ == "__main__":
    sol = Solution()
    assert sol.minSubArrayLen(1, [1]) == 1
    assert sol.minSubArrayLen(2, [1]) == 0
    assert sol.minSubArrayLen(1, [1, 2, 3]) == 1
    assert sol.minSubArrayLen(5, [1, 2, 3]) == 2
    assert sol.minSubArrayLen(3, [1, 1, 1, 2]) == 2
    assert sol.minSubArrayLen(9, [1, 1, 1, 2]) == 0

# Explanation: the code goes through every possible subarray to find the
# shortest one whose sum is >= target, and if none are found, returns 0
# Time: O(n^2), n = len(nums)
# Aux space, excluding output and input: O(1)
# Total space, including output, excluding input: O(1)

# Learning lessons (done after completing all of above in 15 mins):
#   - I now realise there is an O(n) time solution. My rewrite is below:
#
# def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#     # Time: O(n), n = len(nums)
#     # Aux space, excluding output and input: O(1)
#     # Total space, including output, excluding input: O(1)
#     left = 0
#     total = 0
#     best = None
#     for right, num in enumerate(nums):
#         total += num
#         while total >= target:
#             length = right - left + 1
#             best = length if not best else min(best, length)
#             total -= nums[left]
#             left += 1    
#     return 0 if not best else best
 
        









