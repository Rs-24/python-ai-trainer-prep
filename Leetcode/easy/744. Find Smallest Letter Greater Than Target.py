# Time to write all of below including tests, explanation and time and aux
# and total space: 7 mins

# Problem: https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Time: O(log n), n = len(letters)
        # Space: O(1)
        l, r = 0, len(letters) - 1
        out = letters[0]
        while l <= r:
            mid = (l + r) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                out = letters[mid]
                r = mid - 1
        return out

# Alternative method: 
from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Time: O(log n), n = len(letters)
        # Space: O(1)
        l, r = 0, len(letters)
        while l < r:
            mid = (l + r) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return letters[l % len(letters)]


