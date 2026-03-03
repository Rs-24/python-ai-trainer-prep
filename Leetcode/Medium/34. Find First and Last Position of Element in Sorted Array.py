# Time to write all of below including tests, explanation and time and aux
# and total space: 24 mins

# Problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return[-1, -1]
        def search(x: int) -> int:
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < x:
                    l = mid + 1
                else:
                    r = mid
            return l
        start = search(target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = search(target + 1) - 1
        return [start, end]

if __name__ == "__main__":
    sol = Solution()
    assert sol.searchRange([], 0) == [-1, -1]
    assert sol.searchRange([], -1) == [-1, -1]
    assert sol.searchRange([], 1) == [-1, -1]
    assert sol.searchRange([1], 1) == [0, 0]
    assert sol.searchRange([1], 2) == [-1, -1]
    assert sol.searchRange([1, 1, 1], 1) == [0, 2]
    assert sol.searchRange([-1, 0, 1, 2], 2) == [3, 3]
    assert sol.searchRange([-1, 0, 1, 2], 3) == [-1, -1]

# Explanation: the code does a left bounded binary search twice to find the
# first and last index of target
# Time: O(log n), n = len(nums)
# Space: excluding output: O(1)


