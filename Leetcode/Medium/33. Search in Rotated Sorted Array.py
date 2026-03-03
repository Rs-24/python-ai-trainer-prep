# Time to write all of below including tests, explanation and time and aux
# and total space: 13 mins

# Problem: https://leetcode.com/problems/search-in-rotated-sorted-array/description/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

if __name__ == "__main__":
    sol = Solution()
    assert sol.search([1], 1) == 0
    assert sol.search([1], 0) == -1
    assert sol.search([-1, 0, 1, 2, 3], 2) == 3
    assert sol.search([-1, 0, 1, 2, 3], 4) == -1
    assert sol.search([1, 2, 3, -1, 0], 2) == 1
    assert sol.search([1, 2, 3, -1, 0], -1) == 3
    assert sol.search([1, 2, 3, -1, 0], 4) == -1

# Explanation: the code does a binary search, and in each iteration
# checks if the left half is sorted and if so if target is in it, and adjusts
# l and r accordingly
# Time: O(log n), n = len(nums)
# Space: O(1)


