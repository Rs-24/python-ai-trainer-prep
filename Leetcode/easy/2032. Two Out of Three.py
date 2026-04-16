# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/two-out-of-three/description/

from typing import List
from collections import Counter

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        # Time: O(m + n + k), m = len(nums1), n = len(nums2), k = len(nums3)
        # Aux space: O(m + n + k)
        c = Counter()
        c.update(set(nums1))
        c.update(set(nums2))
        c.update(set(nums3))
        return [num for num, freq in c.items() if freq >= 2]


