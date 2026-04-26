# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/description/

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # Time: O(1)
        # Space: O(1)
        return sorted(s1[0::2]) == sorted(s2[0::2]) and sorted(s1[1::2]) == sorted(s2[1::2])


