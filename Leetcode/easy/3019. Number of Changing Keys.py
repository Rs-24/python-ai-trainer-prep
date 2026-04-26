# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/number-of-changing-keys/description/

class Solution:
    def countKeyChanges(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        changes = 0
        prev = None
        for ch in s:
            if prev and prev != ch.lower():
                changes += 1
            prev = ch.lower()
        return changes


