# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/count-asterisks/description/

class Solution:
    def countAsterisks(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        in_pair = False
        count = 0
        for ch in s:
            if ch == "|":
                in_pair = not in_pair
            elif ch == "*" and not in_pair:
                count += 1
        return count


