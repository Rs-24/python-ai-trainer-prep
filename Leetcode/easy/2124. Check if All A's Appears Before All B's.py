# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/description/

class Solution:
    def checkString(self, s: str) -> bool:
        # Time: O(n), n = len(s)
        # Space: O(1)
        b_found = False
        for ch in s:
            if ch == "a" and b_found:
                return False
            elif ch == "b":
                b_found = True
        return True


