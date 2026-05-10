# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/description/

class Solution:
    def minChanges(self, n: int, k: int) -> int:
        # Time: O(1)
        # Space: O(1)
        if (n & k) != k:
            return -1
        return (n ^ k).bit_count()
        

