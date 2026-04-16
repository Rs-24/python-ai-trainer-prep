# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/kth-distinct-string-in-an-array/description/

from typing import List
from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # Time: O(n), n = len(arr)
        # Space: O(n)
        freq = Counter(arr)
        for word in arr:
            if freq[word] == 1:
                k -= 1
            if k == 0:
                return word
        return ""


