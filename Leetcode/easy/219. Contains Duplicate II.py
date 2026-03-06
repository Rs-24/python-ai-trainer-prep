# Time to write all of below including tests, explanation and time and aux
# and total space: 12 mins

# Problem: https://leetcode.com/problems/contains-duplicate-ii/description/

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Time: O(m), m = number of numbers processed, worst case O(n),
        # n = len(nums)
        # Space: O(m), worst case O(n)
        seen = {}
        for i, num in enumerate(nums):
            if num in seen and abs(seen[num] - i) <= k:
                return True
            seen[num] = i
        return False

# set() method:
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Time: O(m), m = number of numbers processed, worst case O(n),
        # n = len(nums)
        # Space: O(min(n, k))
        seen = set()
        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            if len(seen) > k:
                seen.remove(nums[i - k])
        return False


