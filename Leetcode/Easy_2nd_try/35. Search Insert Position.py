# Time to write all of below including tests, why the solution works and time 
# and space complexity: 16 mins

# Problem: https://leetcode.com/problems/search-insert-position/description/

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target <= nums[0]:
                return 0
            else:
                return 1
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid
            else:
                l = mid + 1
        return l

if __name__ == "__main__":
    sol = Solution()
    assert sol.searchInsert([1], 1) == 0
    assert sol.searchInsert([1], 2) == 1
    assert sol.searchInsert([2], -1) == 0
    assert sol.searchInsert([-1, 0, 1], 0) == 1
    assert sol.searchInsert([0, 1], -1) == 0
    assert sol.searchInsert([1, 2, 3, 4, 5], 1) == 0
    assert sol.searchInsert([1, 2, 3, 4, 5], 2) == 1
    assert sol.searchInsert([1, 3, 4, 5, 6], 2) == 1
    assert sol.searchInsert([1, 2, 3, 4, 5], 4) == 3
    assert sol.searchInsert([1, 2, 3, 4, 6], 5) == 4

# Explanation: the code uses a lower bounded binary search to find the index 
# where target is, and if it is not in nums, returns the left pointer once the
# loop ends
# Time: O(log n), n = len(nums)
# Aux space, excluding output and input: O(1)
# Total space, including output, excluding input: O(1)

# Learning lessons (done after completing all of above in 16 mins):
#   - I now realise my solution can be improved, my rewrite is below:
#
# def searchInsert(self, nums: List[int], target: int) -> int:
#     # Time: O(log n), n = len(nums)
#     # Aux space, excluding output and input: O(1)
#     # Total space, including output, excluding input: O(1)
#     l, r = 0, len(nums) - 1
#     while l <= r:
#         mid = (l + r) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             l = mid + 1
#         else:
#             r = mid - 1
#     return l



