# Time to write all of below including tests, explanation and time and aux
# and total space: 24 mins

# Problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        out = []
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                out.append(mid)
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if len(out) == 0:
            return [-1, -1]
        else:
            i = out[0]
            if i == 0:
                return [i, i + 1]
            elif i == len(nums) - 1:
                return [i - 1, i]
            elif nums[i - 1] == nums[i]:
                return [i - 1, i]
            else:
                return [i, i + 1]

if __name__ == "__main__":
    sol = Solution()
    assert sol.searchRange([], 0) == [-1, -1]
    assert sol.searchRange([], 2) == [-1, -1]
    assert sol.searchRange([], -1) == [-1, -1]
    assert sol.searchRange([], -1) == [-1, -1]
    assert sol.searchRange([-1, 0, 1, 1], 2) == [-1, -1]
    assert sol.searchRange([-1, 0, 0, 1, 1], 0) == [1, 2]
    assert sol.searchRange([-1, -1, 0, 1, 1], -1) == [0, 1]

# Explanation: the code does a binary search to find the index of target, and
# if it is not found returns [-1, -1]. If the index is found, then either 
# [i, i + 1] or [i - 1, i] is returned
# Time: O(log n), n = len(nums)
# Aux space, excluding output and input: O(1)
# Total space, including output, excluding input: O(1)

# Learning lessons (done after completing all of above in 24 mins):
#   - I now realise my solution is incorrect. My rewrite is below:
#
# def searchRange(self, nums: List[int], target: int) -> List[int]:
#     # Time: O(log n), n = len(nums)
#     # Aux space, excluding output and input: O(1)
#     # Total space, including output, excluding input: O(1)
#     def lower_bound(x: int) -> int:
#         l, r = 0, len(nums)
#         while l < r:
#             mid = (l + r) // 2
#             if nums[mid] < x:
#                 l = mid + 1
#             else:
#                 r = mid
#         return l
#     first = lower_bound(target)
#     if first == len(nums) or nums[first] != target:
#         return [-1, -1]
#     last = lower_bound(target + 1) - 1
#     return [first, last]
#
#   - Additionally, my tests could have been improved, my rewrite is below:
#
# if __name__ == "__main__":
#     sol = Solution()
#     assert sol.searchRange([], 0) == [-1, -1]
#     assert sol.searchRange([], -1) == [-1, -1]
#     assert sol.searchRange([], 1) == [-1, -1]
#     assert sol.searchRange([1], 1) == [0, 0]
#     assert sol.searchRange([1], 2) == [-1, -1]
#     assert sol.searchRange([1, 1, 1], 1) == [0, 2]
#     assert sol.searchRange([-1, 0, 1, 2], 2) == [3, 3]
#     assert sol.searchRange([-1, 0, 1, 2], 3) == [-1, -1]








