# Time to write all of below including tests, why the solution works and time 
# and space complexity: 19 mins

# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l

if __name__ == "__main__":
    sol = Solution()

    l1 = [1]
    assert sol.removeDuplicates(l1) == 1
    assert l1 == [1]
    
    l1 = [1, 2]
    assert sol.removeDuplicates(l1) == 2
    assert l1 == [1, 2]

    l1 = [-1, 0, 1, 1]
    assert sol.removeDuplicates(l1) == 3
    assert l1[:3] == [-1, 0, 1]

    l1 = [1, 2, 2, 3, 4, 5, 5, 6, 7]
    assert sol.removeDuplicates(l1) == 7
    assert l1[:7] == [1, 2, 3, 4, 5, 6, 7]

# Explanation: the code iterates through the list using a left and right
# pointer, and compares each value to its previous value. If they are 
# different, the value at the left pointer is set to the value at the
# right pointer, and the left pointer is incremented
# Time: O(n), n = len(nums)
# Space: O(1)


