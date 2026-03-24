# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/intersection-of-two-arrays/description/

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Time: O(n + m), n = len(nums1), m = len(nums2)
        # Space, excluding output: O(n + m)
        return list(set(nums1) & set(nums2))

# Clearer version: 
from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Time: O(n + m), n = len(nums1), m = len(nums2)
        # Space, excluding output: O(n + m)
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1.intersection(set2))
        

