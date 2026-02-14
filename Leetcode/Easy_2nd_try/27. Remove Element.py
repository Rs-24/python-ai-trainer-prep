# Time to write all of below including tests, why the solution works and time 
# and space complexity: 18 mins

# Problem: https://leetcode.com/problems/remove-element/description/ 

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        return l

if __name__ == "__main__":
    sol = Solution()

    l1 = []
    assert sol.removeElement(l1, 1) == 0
    assert l1[:0] == []

    l1 = [1]
    assert sol.removeElement(l1, 1) == 0
    assert l1[:0] == []

    l1 = [1]
    assert sol.removeElement(l1, 2) == 1
    assert l1[:1] == [1]

    l1 = [0, 1, 2, 3]
    assert sol.removeElement(l1, 0) == 3
    assert sorted(l1[:3]) == sorted([1, 2, 3])
    
    l1 = [0, 1, 2, 3]
    assert sol.removeElement(l1, 1) == 3
    assert sorted(l1[:3]) == sorted([0, 2, 3])
    
    l1 = [1, 2, 2, 3, 3, 4, 5]
    assert sol.removeElement(l1, 2) == 5
    assert sorted(l1[:5]) == sorted([1, 3, 3, 4, 5])
    
# Explanation: the code iterates through the list with a left and right
# pointer, and if the current value is not equal to val, then the value
# at the left pointer is set to the value at the right pointer, and the
# left pointer is incremented
# Time: O(n), n = len(nums)
# Aux space, excluding output and input: O(1)
# Total space, including output, excluding input: O(1)

# Learning lessons (done after completing all of above in 18 mins):
#   - No major learning lessons


