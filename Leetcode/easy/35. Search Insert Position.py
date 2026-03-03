# Time to write all of below including tests, why the solution works and time 
# and space complexity: 16 mins

# Problem: https://leetcode.com/problems/search-insert-position/description/

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
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

# Explanation: the code performs a binary search and if target is not in the
# list, returns the left pointer
# Time: O(log n), n = len(nums)
# Space: O(1)


