# Time to write all of below including tests, explanation and time and aux
# and total space: 9 mins

# Problem: https://leetcode.com/problems/contains-duplicate/

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

if __name__ == "__main__":
    sol = Solution()
    assert sol.containsDuplicate([1]) == False
    assert sol.containsDuplicate([-1, 0, 1]) == False
    assert sol.containsDuplicate([1, 2, 3, 4, 4]) == True
    assert sol.containsDuplicate([1, 1, 1]) == True

# Explanation: the code stores seen values in a set, and if the current
# number is in the set, then True is returned
# Time: O(k), k = number of numbers processed, worst case O(n), n = len(nums)
# Space: O(k), worst case O(n)

# One-liner method:
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time: O(n), n = len(nums)
        # Space: O(k), k = number of distinct values, worst case O(n)
        return len(set(nums)) != len(nums)


